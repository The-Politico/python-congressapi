from marshmallow import Schema, fields, post_load

from .models import Committee, CommitteeMember


class CommitteeMemberSchema(Schema):
    id = fields.Str()
    name = fields.Str()
    api_uri = fields.Url()
    party = fields.Str()
    rank_in_party = fields.Integer()
    state = fields.Str()
    note = fields.Str()
    begin_date = fields.Str()

    @post_load
    def make_member(self, data):
        return CommitteeMember(**data)


class CommitteeSchema(Schema):
    congress = fields.Str()
    chamber = fields.Str()
    committee = fields.Str()
    num_results = fields.Integer()
    chairman_id = fields.Str()
    ranking_member_id = fields.Str()
    current_members = fields.Nested(CommitteeMemberSchema, many=True)
    former_members = fields.Nested(CommitteeMemberSchema, many=True)

    @post_load
    def make_committee(self, data):
        return Committee(**data)
