if (!window.shiva) {
    var println = require('./modules/helpers').println;
    var sender = require('./modules/sender');

    var SERVER_NAME = '{{server}}';

    println(SERVER_NAME);

    window.shiva = sender(SERVER_NAME);
}
