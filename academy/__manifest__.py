{
    "name": "Academy B&F",
    "category": "Website",
    "description": "Generic controller for web form",
    "author": "Vauxoo",
    "license": "LGPL-3",
    "version": "16.0.1.0.0",
    "depends": ["website_sale"],
    "data": ["security/ir.model.access.csv", "data/academy_menus.xml", "views/templates.xml", "views/views.xml"],
    "demo": ["demo/demo_data.xml"],
    "assets": {
        "web.assets_frontend": [
            "academy/static/src/js/animal.js",
            "academy/static/src/js/dog.js",
            "academy/static/src/js/hamster.js",
            "academy/static/src/js/counter.js",
            "academy/static/src/js/demo_rpc.js",
        ],
        "web.assets_backend": ["academy/static/src/tests/tours/academy_tour.js"],
    },
    "application": True,
    "installable": True,
    "auto_install": False,
}
