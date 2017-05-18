"""
Class methods for committees.

{congress}/{chamber}/committees.json
{congress}/{chamber}/committees/{committee-id}.json
"""
import os
from congressapi.committees.schema import CommitteeSchema


class CommitteesClass(object):
    @staticmethod
    def _deserialize_committees_membership(response):
        committee = response[0]
        data, errors = CommitteeSchema().load(committee)
        return data

    def _deserialize_committees(self, response):
        return response

    def committees(self, chamber, committee_id=None):
        if committee_id:
            uri = os.path.join(
                self.CONGRESS,
                chamber,
                'committees',
                '{}.json'.format(committee_id)
            )
            response = self._make_request(uri)
            return self._deserialize_committees_membership(response)
        else:
            uri = os.path.join(
                self.CONGRESS,
                chamber,
                'committees.json'
            )
            response = self._make_request(uri)
            return self._deserialize_committees(response)
