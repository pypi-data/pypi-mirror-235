from pathlib import Path

import pytest

from fcsv_parser.io import load_fcsv
from fcsv_parser.parser import parse_fcsv

# -------------------------------------------------------------------------


def test_parse_fcsv_coords() -> None:
    """Test fails if unsupported coordinate system."""
    file_path = Path(__file__).parent / "fixtures" / "test_wrong_coords.fcsv"
    lines = load_fcsv(file_path)

    with pytest.raises(ValueError):
        _ = parse_fcsv(lines)


# -------------------------------------------------------------------------


def test_parse_fcsv_2d() -> None:
    """Test parser for 2D data."""
    file_path = Path(__file__).parent / "fixtures" / "test_2D.fcsv"
    lines = load_fcsv(file_path)
    fiducial = parse_fcsv(lines)

    assert fiducial["F-1"] == (-170.167, -432.176, 0.000)
    assert fiducial["F-2"] == (-410.542, -441.791, 0.000)
    assert fiducial["F-3"] == (-679.763, -461.021, 0.000)
    assert fiducial["F-4"] == (-581.209, -691.782, 0.000)


# -------------------------------------------------------------------------


def test_parse_fcsv_3d() -> None:
    """Test parser for 3D data."""
    file_path = Path(__file__).parent / "fixtures" / "test_3D.fcsv"
    lines = load_fcsv(file_path)
    fiducial = parse_fcsv(lines)

    assert fiducial["F-1"] == (-98.054, -178.580, 1782.000)
    assert fiducial["F-2"] == (-327.613, -203.819, 1782.000)
    assert fiducial["F-3"] == (-130.505, -358.862, 1782.000)
    assert fiducial["F-4"] == (-361.265, -363.669, 1782.000)
    assert fiducial["F-5"] == (-128.101, -116.082, 2508.000)
    assert fiducial["F-6"] == (-356.458, -140.120, 2508.000)
    assert fiducial["F-7"] == (-118.486, -311.988, 2508.000)
    assert fiducial["F-8"] == (-369.678, -348.045, 2508.000)
