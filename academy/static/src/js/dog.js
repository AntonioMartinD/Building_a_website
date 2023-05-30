odoo.define("academy.dog", function (require) {
    "use strict";

    var animal = require("academy.animal");

    var Dog = animal.extend({
        move: function () {
            this.bark();
            this._super.apply(this, arguments);
        },
        bark: function () {
            console.log("Woof!");
        },
    });

    var dog = new Dog();
    dog.move();

    return Dog;
});
