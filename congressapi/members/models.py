class CongressionalMember(object):
    def __init__(
        self, id, api_uri, first_name, middle_name, last_name, party,
        leadership_role, twitter_account, facebook_account, govtrack_id,
        cspan_id, votesmart_id, icpsr_id, crp_id, google_entity_id,
        url, rss_url, domain, in_office, dw_nominate, ideal_point,
        seniority, next_election, total_votes, missed_votes, total_present,
        ocd_id, office, phone, state,
        # Missing data from some members:
        missed_votes_pct=None, votes_with_party_pct=None
    ):
        self.id = id
        self.api_uri = api_uri
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.party = party
        self.leadership_role = leadership_role
        self.twitter_account = twitter_account
        self.facebook_account = facebook_account
        self.govtrack_id = govtrack_id
        self.cspan_id = cspan_id
        self.votesmart_id = votesmart_id
        self.icpsr_id = icpsr_id
        self.crp_id = crp_id
        self.google_entity_id = google_entity_id
        self.url = url
        self.rss_url = rss_url
        self.domain = domain
        self.in_office = in_office
        self.dw_nominate = dw_nominate
        self.ideal_point = ideal_point
        self.seniority = seniority
        self.next_election = next_election
        self.total_votes = total_votes
        self.missed_votes = missed_votes
        self.total_present = total_present
        self.ocd_id = ocd_id
        self.office = office
        self.phone = phone
        self.state = state
        self.missed_votes_pct = missed_votes_pct
        self.votes_with_party_pct = votes_with_party_pct


class HouseMember(CongressionalMember):
    def __init__(
        self, fax, district, youtube_account,
        contact_form, *args, **kwargs
    ):
        self.fax = fax
        self.district = district
        self.youtube_account = youtube_account
        self.contact_form = contact_form
        super(HouseMember, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<HouseMember({self.last_name!s}-{self.state!s})>'.format(self=self) #noqa


class SenateMember(CongressionalMember):
    def __init__(self, senate_class, state_rank, lis_id, *args, **kwargs):
        self.senate_class = senate_class
        self.state_rank = state_rank
        self.lis_id = lis_id
        super(SenateMember, self).__init__(*args, **kwargs)

    def __repr__(self):
        return '<SenateMember({self.last_name!s}-{self.state!s})>'.format(self=self) #noqa


class Chamber(object):
    def __init__(self, congress, chamber, members, num_results, offset):
        self.congress = congress
        self.chamber = chamber
        self.num_results = num_results
        self.offset = offset
        self.members = members

    def __repr__(self):
        return '<Chamber({self.congress!s}th Congress - The {self.chamber!s})>'.format(self=self) #noqa


class Senate(Chamber):
    pass


class House(Chamber):
    pass
