from typing import Any, Callable, TypeVar

import requests
from requests import Response
import seaplane_framework.api
from seaplane_framework.api import ApiClient

from ..configuration import Configuration, config
from ..logging import log
from ..model.errors import HTTPError
from .api_http import SDK_HTTP_ERROR_CODE
from .token_api import TokenAPI

T = TypeVar("T")


def provision_req(token_api: TokenAPI) -> Callable[[Callable[[str], Response]], Any]:
    """
    Returns an object that can make token-authenticated API calls passed in as
    function parameters, mapping the results type based on `Content-Type`.

    :param token_api: the TokenAPI instance to use
    :returns: -- A function of type `((token) -> Response) -> Any` that can wrap
        token-requiring HTTP calls in a way that handles reauthentication
        correctly and parses the result based on `Content-Type`.
    """
    return lambda request: provision_token(token_api)(lambda token: _map_response(request(token)))


def provision_token(token_api: TokenAPI) -> Callable[[Callable[[str], T]], T]:
    """
    Returns an object that can make token-authenticated API calls passed in as
    function parameters.

    :param token_api: the TokenAPI instance to use
    :returns: -- A function of type `((token) -> T) -> T` that can wrap
        token-requiring functions in a way that handles reauthentication
        correctly.
    """

    def _req(request: Callable[[str], T]) -> T:
        try:
            return request(_extract_token(token_api))
        except HTTPError as e:
            _renew_if_failed(token_api, e)
            return request(_extract_token(token_api))
        except requests.exceptions.RequestException as err:
            _renew_if_failed(token_api, _map_request_exception(err))
            return request(_extract_token(token_api))

    return _req


def _map_response(response: Response) -> Any:
    """
    Extracts the response payload of an HTTP call, parsing it if possible based
    on the `Content-Type` header.

    :returns: A `bytes` payload if `Content-Type` is
        `application/octect-stream`, a JSON payload for `application/json`, and
        a `str` for anything else.
    """
    if not response.ok:
        body_error = response.text
        log.error(f"Request Error: {body_error}")
        raise HTTPError(response.status_code, body_error)
    if response.headers.get("content-type") == "application/json":
        return response.json()
    elif response.headers.get("content-type") == "application/octet-stream":
        return response.content
    else:
        return response.text


def _renew_if_failed(token_api: TokenAPI, http_error: HTTPError) -> None:
    """
    Attempts to renew a token if the given error calls for it.
    """
    if http_error.status != 401 or not token_api.auto_renew:
        raise http_error
    log.info("Auto-Renew, renewing the token...")
    token_api.renew_token()


def _extract_token(token_api: TokenAPI) -> str:
    """
    Pulls a token out of the token API, requesting one if necessary.
    """
    if token_api.access_token is None:
        token_api._request_access_token()
    return token_api.access_token or ""  # Will always be set by `_request_access_token()`


def _map_request_exception(err: requests.exceptions.RequestException) -> HTTPError:
    """
    Maps a raw `requests` exception into a Seaplane `HTTPError`.
    """
    log.error(f"Request exception: {str(err)}")
    status_code: int = SDK_HTTP_ERROR_CODE
    if err.response:
        status_code = err.response.status_code
    return HTTPError(status_code, str(err))


def get_pdk_client(access_token: str, cfg: Configuration = config) -> ApiClient:
    """
    Constructs a Seaplane PDK ApiClient from the given access token.
    """
    from .. import __version__

    pdk_config = cfg.get_platform_configuration()
    pdk_config.access_token = access_token
    client = ApiClient(pdk_config)
    client.set_default_header("X-Seaplane-Sdk-Version", __version__)
    client.set_default_header("X-Seaplane-Pdk-Version", seaplane_framework.api.__version__)
    return client
