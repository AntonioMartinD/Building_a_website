from odoo import http

from odoo.addons.website_sale.controllers.main import WebsiteSale


class Academy(http.Controller):
    @http.route("/academy/academy/", auth="public", website=True)
    def index(self, **kw):
        teachers = http.request.env["academy.teachers"]
        return http.request.render("academy.index", {"teachers": teachers.search([])})

    @http.route("/academy/<name>", auth="public", website=True)
    def teacher(self, name):
        return "<h1>{}<h1>".format(name)

    @http.route("/academy/<model('academy.teachers'):teacher>", auth="public", website=True)
    def obj_teacher(self, teacher):
        return http.request.render("academy.biography", {"person": teacher})

    @http.route("/academy/search_teacher", type="json", auth="public", website=True)
    def search_teacher(self, **args):
        teacher_obj = http.request.env["academy.teachers"]
        teachers = teacher_obj.search_read([("id", "=", args.get("teacher_id", False))], fields=["biography"])
        return teachers


class WebsiteSaleInh(WebsiteSale):
    @http.route()
    def shop(self, page=0, category=None, search="", min_price=0.0, max_price=0.0, ppg=False, **post):
        res = super().shop(
            page=page, category=category, search=search, min_price=min_price, max_price=max_price, ppg=ppg, **post
        )
        res.qcontext["categories"] = res.qcontext["categories"].sorted(key=lambda r: r.name)
        res.qcontext["search"] = "ipad"
        return res
