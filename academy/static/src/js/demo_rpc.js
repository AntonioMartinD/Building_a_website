odoo.define("academy.demo_rpc", function (require) {
    "use strict";

    var core = require("web.core");
    var publicWidget = require("web.public.widget");
    require("web.dom_ready");

    publicWidget.registry.RpcButton = publicWidget.Widget.extend({
        selector: ".rpc-container",

        events: {
            "click .rpc-button": "onClick",
        },

        onClick: function (ev) {
            console.log("Clicked");
            this._rpc({
                model: "academy.teacher",
                method: "search_read",
                args: [[["id", "=", this.$el.data("teacher-id")]], ["biography"]],
            }).then(function (data) {
                if (data.length) {
                    $(".biography").html(data[0].biography);
                }
            });
        },
    });

    var RpcButton = new publicWidget.registry.RpcButton(this);
    RpcButton.appendTo($(".rpc-container"));

    return publicWidget.registry.RpcButton;
});
