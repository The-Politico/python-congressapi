class CommitteeMember(object):
    def __init__(
        self, id, name, api_uri, party, rank_in_party,
        state, note, begin_date
    ):
        self.id = id
        self.name = name
        self.api_uri = api_uri
        self.party = party
        self.rank_in_party = rank_in_party
        self.state = state
        self.note = note
        self.begin_date = begin_date

    def __repr__(self):
        return '<CommitteeMember(name={self.name!r})>'.format(self=self)


class Committee(object):
    def __init__(
        self, congress, chamber, committee, num_results, chairman_id,
        ranking_member_id, current_members, former_members
    ):
        self.congress = congress
        self.chamber = chamber
        self.committee = committee
        self.num_results = num_results
        self.chairman_id = chairman_id
        self.ranking_member_id = ranking_member_id
        self.current_members = current_members
        self.former_members = former_members

    def __repr__(self):
        return '<Committee(committee={self.committee!r})>'.format(self=self)
