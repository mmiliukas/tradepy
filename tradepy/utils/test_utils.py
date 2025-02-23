from .split_into_chunks import split_into_chunks


def test_split_into_chunks():
    chunks = split_into_chunks([1, 2, 3, 4, 5], 1)
    assert chunks == [[1], [2], [3], [4], [5]]

    chunks = split_into_chunks([1, 2, 3, 4, 5], 2)
    assert chunks == [[1, 2], [3, 4], [5]]

    chunks = split_into_chunks([1, 2, 3, 4, 5], 6)
    assert chunks == [[1, 2, 3, 4, 5]]
