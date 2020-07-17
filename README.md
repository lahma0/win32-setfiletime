# win32-setfiletime

[![Pypi version](https://img.shields.io/pypi/v/win32-setfiletime.svg)](https://pypi.python.org/pypi/win32-setfiletime) [![Python version](https://img.shields.io/badge/python-3.5%2B-blue.svg)](https://pypi.python.org/pypi/win32-setfiletime) [![Build status](https://img.shields.io/travis/com/lahma0/win32-setfiletime/master.svg)](https://travis-ci.com/lahma0/win32-setfiletime) [![License](https://img.shields.io/github/license/lahma0/win32-setfiletime.svg)](https://github.com/lahma0/win32-setfiletime/blob/master/LICENSE)

A small Python utility to set file creation/modified/accessed time on Windows.

## Installation

```shell
pip install win32-setfiletime
```

## Usage

```python
from win32_setfiletime import setctime, setmtime, setatime

setctime("my_file.txt", 1561675987.509)
setmtime("my_file.txt", 1561675987.509)
setatime("my_file.txt", 1561675987.509)
```
