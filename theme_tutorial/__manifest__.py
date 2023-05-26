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
        "views/layout.xml",
        "views/pages.xml",
        "static/src/snippets/snippets.xml",
        "static/src/snippets/options.xml",
    ],
    "assets": {
        "web.assets_frontend": ["theme_tutorial/static/src/scss/style.scss"],
        "web.assets_editor": ["theme_tutorial/static/src/js/tutorial_editor.js"],
    },
    "installable": True,
    "auto_install": False,
}
