"""
Python lib for ProPublica's congress API.

Add more stuff here.
"""
import os
import requests


from .committees import CommitteesClass
from .members import MembersClass


class BaseCongressClient(object):
    BASE_URI = "https://api.propublica.org/congress/v1/"
    API_KEY = ""
    API_KEY_PARAM = "x-api-key"

    def __init__(self, api_key, base_uri=None):
        self.API_KEY = api_key
        self.BASE_URI = base_uri or BaseCongressClient.BASE_URI

    def _make_request(self, uri_path, params=None):
        headers = {
            self.API_KEY_PARAM: self.API_KEY
        }
        response = requests.get(
            os.path.join(self.BASE_URI, uri_path),
            params=params,
            headers=headers
        )
        # TODO: Catch 403 errors with bad API key
        return response.json()['results']


class Congress(BaseCongressClient, CommitteesClass, MembersClass):
    CONGRESS = '115'

    def __init__(self, congress=None, **kwargs):
        self.CONGRESS = congress or Congress.CONGRESS
        super(Congress, self).__init__(**kwargs)
