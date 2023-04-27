from marshmallow import Schema, fields

class TodoSchema(Schema):
    id = fields.Int(dump_only=True)
    task = fields.Str(required=True)
    status = fields.Str(required=True)


class TodoUpdateSchema(Schema):
    status = fields.Str()