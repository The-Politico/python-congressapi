from marshmallow import Schema, fields, post_load

from congressapi.common import NullableInteger

from .models import House, HouseMember, Senate, SenateMember


class CongressionalMemberSchema(Schema):
    id = fields.Str(required=True)
    api_uri = fields.Url(required=True)
    first_name = fields.Str(required=True)
    middle_name = fields.Str(missing=None)
    last_name = fields.Str(required=True)
    party = fields.Str()
    leadership_role = fields.Str()
    twitter_account = fields.Str()
    facebook_account = fields.Str()
    govtrack_id = fields.Str()
    cspan_id = fields.Str()
    votesmart_id = fields.Str()
    icpsr_id = fields.Str()
    crp_id = fields.Str()
    google_entity_id = fields.Str()
    url = fields.Str()  # Not validating as Url
    rss_url = fields.Str()  # Not validating as Url
    domain = fields.Str()
    in_office = fields.Str()
    dw_nominate = fields.Str()
    ideal_point = fields.Str()
    seniority = fields.Int()
    next_election = fields.Str()
    total_votes = NullableInteger(missing=None)
    missed_votes = NullableInteger(missing=None)
    total_present = NullableInteger(missing=None)
    ocd_id = fields.Str()
    office = fields.Str()
    phone = fields.Str()
    state = fields.Str()
    missed_votes_pct = fields.Float()
    votes_with_party_pct = fields.Float()


class SenateMemberSchema(CongressionalMemberSchema):
    senate_class = fields.Int()
    state_rank = fields.Str()
    lis_id = fields.Str()

    @post_load
    def make_member(self, data):
        return SenateMember(**data)


class HouseMemberSchema(CongressionalMemberSchema):
    fax = fields.Str()
    district = fields.Str()
    youtube_account = fields.Str()
    contact_form = fields.Str()

    @post_load
    def make_member(self, data):
        return HouseMember(**data)


class HouseSchema(Schema):
    congress = fields.Str()
    chamber = fields.Str()
    num_results = fields.Int()
    offset = fields.Int()
    members = fields.Nested(HouseMemberSchema, many=True)

    @post_load
    def make_chamber(self, data):
        return House(**data)


class SenateSchema(Schema):
    congress = fields.Str()
    chamber = fields.Str()
    num_results = fields.Int()
    offset = fields.Int()
    members = fields.Nested(SenateMemberSchema, many=True)

    @post_load
    def make_chamber(self, data):
        return Senate(**data)
