from pathlib import Path

import pytest

from fcsv_parser.io import load_fcsv

# -------------------------------------------------------------------------


def test_load_fcsv_suffix() -> None:
    """Test fails on incorrect suffix."""
    file_path = Path(__file__).parent / "fixtures" / "test.csv"

    with pytest.raises(ValueError):
        _ = load_fcsv(file_path)


# -------------------------------------------------------------------------


def test_load_fcsv_non_exist() -> None:
    """Test fails if file not found."""
    file_path = Path(__file__).parent / "fixtures" / "test.fcsv"

    with pytest.raises(FileNotFoundError):
        _ = load_fcsv(file_path)
