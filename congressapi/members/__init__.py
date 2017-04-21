"""
Class methods for members.

{congress}/{chamber}/members.json
"""
import os
from .schema import HouseSchema, SenateSchema
from congressapi.common import DataValidationError, ChamberRequiredError, InvalidChamber


class MembersClass(object):
    @staticmethod
    def _deserialize_house_members(response):
        chamber = response[0]
        data, errors = HouseSchema().load(chamber)
        for k,v in errors.items():
            DataValidationError('IMPORT ERR - {}: {}'.format(k, v))
        return data

    @staticmethod
    def _deserialize_senate_members(response):
        chamber = response[0]
        data, errors = SenateSchema().load(chamber)
        for k,v in errors.items():
            print('IMPORT ERR - {}: {}'.format(k, v))
        return data

    def get_members(self, chamber=None):
        if not chamber:
            raise ChamberRequiredError("You must specify the chamber for this \
method. Valid values are either 'house' or 'senate'.")
        if chamber == 'house':
            uri = os.path.join(
                self.CONGRESS,
                'house',
                'members.json'
            )
            response = self._make_request(uri)
            return self._deserialize_house_members(response)
        elif chamber == 'senate':
            uri = os.path.join(
                self.CONGRESS,
                'senate',
                'members.json'
            )
            response = self._make_request(uri)
            return self._deserialize_senate_members(response)
        else:
            raise InvalidChamber("You supplied an invalid chamber. \
Valid values are either 'house' or 'senate'.")
