from pathlib import Path
from typing import List

VALID_FILE_ENDING = ".fcsv"


def load_fcsv(file_path: Path) -> List[str]:
    if file_path.suffix != VALID_FILE_ENDING:
        raise ValueError(f"Not .fcsv file: {file_path.suffix}")

    with open(file_path) as fp:
        fcsv_lines = fp.readlines()

    return fcsv_lines
