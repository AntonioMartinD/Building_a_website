from odoo import http
from odoo.http import request

from odoo.addons.website_sale.controllers.main import WebsiteSale


class Academy(http.Controller):
    @http.route("/academy/academy/", auth="public", website=True)
    def index(self, **kw):
        teachers = request.env["academy.teacher"]
        return request.render("academy.index", {"teachers": teachers.search([])})

    @http.route("/academy/<name>", auth="public", website=True)
    def teacher(self, name):
        return "<h1>{}<h1>".format(name)

    @http.route("/academy/<model('academy.teacher'):teacher>", auth="public", website=True)
    def obj_teacher(self, teacher):
        return request.render("academy.biography", {"teacher": teacher})

    @http.route("/academy/search_teacher", type="json", auth="public", website=True)
    def search_teacher(self, **args):
        teacher_obj = request.env["academy.teacher"]
        teachers = teacher_obj.search_read([("id", "=", args.get("teacher_id", False))], fields=["biography"])
        return teachers


class WebsiteSaleInh(WebsiteSale):
    @http.route()
    def shop(self, page=0, category=None, search="", min_price=0.0, max_price=0.0, ppg=False, **post):
        res = super().shop(
            page=page, category=category, search=search, min_price=min_price, max_price=max_price, ppg=ppg, **post
        )
        res.qcontext["categories"] = res.qcontext["categories"].sorted("name")
        res.qcontext["search"] = "ipad"
        return res
