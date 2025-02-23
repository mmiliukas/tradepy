import os
import tempfile

from .download_history import read_history, download_history


def test_download_history():
    with tempfile.TemporaryDirectory() as temp_dir:
        count = download_history(["ACIU"], temp_dir)

        assert count == 1, "only one ticker should be downloaded"
        df = read_history(os.path.join(temp_dir, "ACIU.csv"))

        assert not df.empty, "history shouldn't be empty"
