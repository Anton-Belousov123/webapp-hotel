import os


def is_html_file_exists(path: str) -> bool:
    return os.path.exists(path)
