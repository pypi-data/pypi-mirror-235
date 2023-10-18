# noqa

import hashlib


def remove_prefix(text: str, prefix: str) -> str:
    if text.startswith(prefix):
        return text[len(prefix) :]
    return text


def file_md5(path: str) -> str:
    """
    Gets the MD5 hash of a file by path.
    """

    hasher = hashlib.md5()
    block_size = 4194304  # 4 MB
    with open(path, "rb") as fh:
        while True:
            buffer = fh.read(block_size)
            if not buffer:
                break
            hasher.update(buffer)
    return hasher.hexdigest()
