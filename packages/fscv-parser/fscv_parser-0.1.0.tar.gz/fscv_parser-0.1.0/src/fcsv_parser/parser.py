import enum
import logging
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

SUPPORTED_VERSIONS = ["4.10"]


# -------------------------------------------------------------------------


@enum.unique
class CoordinateSystemMappings(str, enum.Enum):
    RAS = "0"
    LPS = "1"


@enum.unique
class CoordinateSystems(str, enum.Enum):
    RAS = "RAS"
    LPS = "LPS"


# -------------------------------------------------------------------------


@dataclass
class Fiducial:
    """Wrapper for version/coordinate information and fiducials.
    :param version: fcsv version
    :param coordinate system: `LPS or `RPS` coordinates
    :param fiducial_dict: dict of description strings and coordinate tuples
    """

    version: str
    coordinate_system: str
    fiducial_dict: Dict[str, Tuple[float, float, float]] = field(default_factory=dict)

    def __getitem__(self, key: str) -> Tuple[float, float, float]:
        return self.fiducial_dict[key]


# -------------------------------------------------------------------------


def parse_fcsv(fcsv_lines: List[str]) -> Fiducial:
    """Parse list of lines of fcsv data.
    :param fcsv_lines: list of strings to be parsed
    :return: Fiducial dataclass
    """
    version = fcsv_lines[0].split("=")[-1].strip(" ").strip("\n")
    if version not in SUPPORTED_VERSIONS:
        msg = f".fcsv version not supported: {version}"
        logging.warning(msg)

    coordinate_system = fcsv_lines[1].split("=")[-1].strip(" ").strip("\n")
    if coordinate_system == CoordinateSystemMappings.RAS:
        coordinate_system = CoordinateSystems.RAS

    elif coordinate_system == CoordinateSystemMappings.LPS:
        coordinate_system = CoordinateSystems.LPS

    else:
        raise ValueError(f"Invalid coordinate system: {coordinate_system}")

    fiducial = Fiducial(version=version, coordinate_system=coordinate_system)

    for line in fcsv_lines[3:]:
        elements = line.split(",")
        description = elements[11]

        x_coord = float(elements[1])
        y_coord = float(elements[2])
        z_coord = float(elements[3])

        fiducial.fiducial_dict[description] = (x_coord, y_coord, z_coord)

    return fiducial
