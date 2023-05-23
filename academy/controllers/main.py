from odoo import http


class Academy(http.Controller):
    @http.route("/academy/academy/", auth="public")
    def index(self, **kw):
        teachers = http.request.env["academy.teachers"]
        return http.request.render("academy.index", {"teachers": teachers.search([])})
