from odoo import fields, models


class Teachers(models.Model):
    _name = "academy.teachers"

    name = fields.Char()
    biography = fields.Html()
