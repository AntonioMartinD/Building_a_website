from odoo import fields, models


class Teachers(models.Model):
    _name = "academy.teacher"

    name = fields.Char()
    biography = fields.Html()
