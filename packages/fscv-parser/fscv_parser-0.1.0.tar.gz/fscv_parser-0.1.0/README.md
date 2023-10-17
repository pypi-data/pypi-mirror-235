# .fcsv Parser
[![Code quality](https://github.com/markpinnock/fcsv-parser/actions/workflows/check_code_quality.yml/badge.svg)](https://github.com/markpinnock/fcsv-parser/actions/workflows/check_code_quality.yml) [![Static typing](https://github.com/markpinnock/fcsv-parser/actions/workflows/check_typing.yml/badge.svg)](https://github.com/markpinnock/fcsv-parser/actions/workflows/check_typing.yml) [![CI tests](https://github.com/markpinnock/fcsv-parser/actions/workflows/run_tests.yml/badge.svg)](https://github.com/markpinnock/fcsv-parser/actions/workflows/run_tests.yml)
[![python](https://img.shields.io/badge/Python-3.8-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Overview
This package provides a simple way to read a markups fiducial point list file (.fcsv) for use in annotations/bounding box creation in medical images. These can be created in an application like [3D Slicer](https://www.slicer.org). The format of these fiducial lists is outlined [here](https://slicer.readthedocs.io/en/latest/developer_guide/modules/markups.html).

## Requirements
This package has been tested with Python 3.8, and currently version 4.10 of the `.fcsv` format is supported. If running the example notebook, a virtual environment should be created and then the requirements in Linux installed using:

```bash
user@account:~/fcsv-parser$ python3 -m fcsv
user@account:~/fcsv-parser$ source fcsv/bin/activate
(fcsv) user@account:~/fcsv-parser$ pip install -r requirements.txt
```

If Windows is used, conda is recommended:

```bash
(base) C:\User\fcsv-parser> conda create -n fcsv python=3.8
(base) C:\User\fcsv-parser> conda activate fcsv
(fcsv) C:\User\fcsv-parser> pip install -r requirements.txt
```

Otherwise all that is needed is to install directly from PyPI into your environment:
```bash
(your-env) user@account:~/fcsv-parser$ pip install fcsv-parser
```

## Usage
Once installed, a fiducial file can be loaded, returning a `dataclass`. The individual fiducials can be accessed with their IDs as you would a `dict`:

```bash
(fcsv) C:\User\fcsv-parser>python
Python 3.8.16 (default, Mar  2 2023, 03:18:16) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from fcsv_parser import read_fcsv
>>> fiducials = read_fcsv("C:\path\to\data")
>>> fiducials["F-1"]:
(170.167, 432.176, -0.0)
```
