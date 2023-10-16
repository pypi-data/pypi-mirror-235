[![Release](https://github.com/grupodyd/python-filapp/actions/workflows/python-publish.yml/badge.svg)](https://github.com/grupodyd/python-filapp/actions/workflows/python-publish.yml)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![pypi](https://badge.fury.io/py/filapp.svg)](https://pypi.org/project/filapp/)
[![PyPI](https://img.shields.io/pypi/pyversions/filapp.svg)](https://pypi.python.org/pypi/filapp)
# python-filapp
Python package for integration of Filapp in other applications

### Supported Python Versions

This library supports the following Python implementations:

- Python 3.8
- Python 3.9
- Python 3.10
- Python 3.11

## Installation

Install from PyPi using [pip](https://pip.pypa.io/en/latest/), a
package manager for Python.

```shell
pip3 install filapp
```

### Test your installation

Try listing your company branches. Save the following code sample to your computer with a text editor. Be sure to update the `auth_token`, and `company_id` variables.

```python3
from filapp import Filapp

# Your Auth Token
client = Filapp(auth_token="your_auth_token", company_id="your_company_id")

branches = client.get_branches()
for branch in branches:
    print(f"Branch ID {branch.id}, name {branch.name}")
```
