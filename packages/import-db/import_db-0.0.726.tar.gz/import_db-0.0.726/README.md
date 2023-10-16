# import_db [![import_db](https://github.com/InnovAnon-Inc/import_db/actions/workflows/pkgrel.yml/badge.svg)](https://github.com/InnovAnon-Inc/import_db/actions/workflows/pkgrel.yml)
Dockerized REST API that connects to MSFRPCD on the Backend to run the import_db Command
==========

[![License Summary](https://img.shields.io/github/license/InnovAnon-Inc/import_db?color=%23FF1100&label=Free%20Code%20for%20a%20Free%20World%21&logo=InnovAnon%2C%20Inc.&logoColor=%23FF1133&style=plastic)](https://tldrlegal.com/license/unlicense#summary)
[![Latest Release](https://img.shields.io/github/commits-since/InnovAnon-Inc/import_db/latest?color=%23FF1100&include_prereleases&logo=InnovAnon%2C%20Inc.&logoColor=%23FF1133&style=plastic)](https://github.com/InnovAnon-Inc/import_db/releases/latest)
[![Lines of Code](https://tokei.rs/b1/github/InnovAnon-Inc/import_db?category=code&color=FF1100&logo=InnovAnon-Inc&logoColor=FF1133&style=plastic)](https://github.com/InnovAnon-Inc/import_db)
[![Repo Size](https://img.shields.io/github/repo-size/InnovAnon-Inc/import_db?color=%23FF1100&logo=InnovAnon%2C%20Inc.&logoColor=%23FF1133&style=plastic)](https://github.com/InnovAnon-Inc/import_db)
[![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/InnovAnon-Inc/import_db?color=FF1100&logo=InnovAnon-Inc&logoColor=FF1133&style=plastic)](https://www.codefactor.io/repository/github/InnovAnon-Inc/import_db)

![Dependent repos (via libraries.io)](https://img.shields.io/librariesio/dependent-repos/pypi/import_db?color=FF1100&style=plastic)
![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/import_db?color=FF1100&style=plastic)
![Libraries.io SourceRank](https://img.shields.io/librariesio/sourcerank/pypi/import_db?style=plastic)
![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/InnovAnon-Inc/import_db?color=FF1100&logoColor=FF1133&style=plastic)

![PyPI - Implementation](https://img.shields.io/pypi/implementation/import_db?color=FF1100&logo=InnovAnon-Inc&logoColor=FF1133&style=plastic)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/import_db?color=FF1100&logo=InnovAnon-Inc&logoColor=FF1133&style=plastic)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/import_db?color=FF1100&logo=InnovAnon-Inc&logoColor=FF1133&style=plastic)
![PyPI - Downloads](https://img.shields.io/pypi/dd/import_db?color=FF1100&logo=InnovAnon-Inc&logoColor=FF1133&style=plastic)
![PyPI - Format](https://img.shields.io/pypi/format/import_db?color=FF1100&logo=InnovAnon-Inc&logoColor=FF1133&style=plastic)
![PyPI - Status](https://img.shields.io/pypi/status/import_db?color=FF1100&logo=InnovAnon-Inc&logoColor=FF1133&style=plastic)
![PyPI - License](https://img.shields.io/pypi/l/import_db?color=FF1100&logo=InnovAnon-Inc&logoColor=FF1133&style=plastic)
![PyPI](https://img.shields.io/pypi/v/import_db?color=FF1100&logo=InnovAnon-Inc&logoColor=FF1133&style=plastic)

[![Tip Me via PayPal](https://img.shields.io/badge/paypal-donate-FF1100.svg?logo=paypal&logoColor=FF1133&style=plastic)](https://www.paypal.me/InnovAnon)

----------

# Build Requirements (TODO)

# Build

```sh
python3 -m build
```

# Install

```sh
TEAMHACK_VERSION=$x.$y.$z \
python3 -m pip install dist/import_db-$TEAMHACK_VERSION-py3-none-any.whl
```

# Test

```sh
pytest
```

# Run

```sh
python3 -m import_db
```

# Build (Docker)

```sh
TEAMHACK_VERSION=$x.$y.$z \
docker build -t "innovanon/import_db:v$TEAMHACK_VERSION" .
```

# Run (Docker)

```sh
docker run -v import-db:/var/teamhack/upload:rw import_db
```

# Usage

```sh
curl -T nmap.xml http://import_db.innovanon.com:65432/upload
```

# InnovAnon, Inc. Proprietary (Innovations Anonymous)
> "Free Code for a Free World!"
==========
![Corporate Logo](https://innovanon-inc.github.io/assets/images/logo.gif)

