from pathlib import Path
from typing import Union

from fcsv_parser.io import load_fcsv
from fcsv_parser.parser import Fiducial, parse_fcsv


def read_fscv(file_path: Union[Path, str]) -> Fiducial:
    if isinstance(file_path, str):
        file_path = Path(file_path)

    fcsv_lines = load_fcsv(file_path)
    return parse_fcsv(fcsv_lines)
