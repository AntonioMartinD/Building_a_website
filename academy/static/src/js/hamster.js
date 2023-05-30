odoo.define("academy.hamster", function (require) {
    var animal = require("academy.animal");

    var DanceMixin = {
        dance: function () {
            console.log("Dancing...");
        },
    };

    var Hamster = animal.extend(DanceMixin, {
        sleep: function () {
            console.log("Sleeping...");
        },
    });

    var hamster = new Hamster();

    hamster.dance();
    hamster.sleep();
});
