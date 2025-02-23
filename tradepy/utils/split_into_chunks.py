from typing import Any


def split_into_chunks(list: list[Any], chunk_size: int) -> list[list[Any]]:
    return [list[i : i + chunk_size] for i in range(0, len(list), chunk_size)]
