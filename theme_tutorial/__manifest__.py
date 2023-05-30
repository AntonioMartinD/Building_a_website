{
    "name": "Theme Tutorial",
    "description": "A theme tutorial app",
    "category": "Theme/Creative",
    "author": "Vauxoo",
    "license": "LGPL-3",
    "version": "16.0.1.0.0",
    "depends": ["website"],
    "data": [
        "data/images.xml",
        "views/templates/layout.xml",
        "views/pages/pages.xml",
        "views/snippets/snippets.xml",
        "views/snippets/options.xml",
    ],
    "assets": {
        "web.assets_frontend": ["theme_tutorial/static/src/scss/main.scss"],
        "web.assets_editor": ["theme_tutorial/static/src/js/tutorial_editor.js"],
    },
    "installable": True,
    "auto_install": False,
}
