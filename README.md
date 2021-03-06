![POLITICO](https://rawgithub.com/The-Politico/src/master/images/logo/badge.png)

# python-congressapi

Python wrapper for [ProPublica's Congress API](https://propublica.github.io/congress-api-docs/). Uses [Marshmallow](http://marshmallow.readthedocs.io) to deserialize API JSON into proper classes.

## Install

Until this library is published on pypi, install from github or yer local:

```bash
$ pip install -e git+https://github.com/The-Politico/python-congressapi.git#egg=python-congressapi
```

## Use

```python
import os

from congressapi import Congress

api_key = os.getenv('PROPUBLICA_CONGRESS_API_KEY', None)
client = Congress(api_key=api_key, congress='115')
senate = client.get_members('senate')

for senator in senate.members:
  print(senator.last_name)
```

See schemas for what's done. Most isn't.
