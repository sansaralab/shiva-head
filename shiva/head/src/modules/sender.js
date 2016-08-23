var SERVER_NAME = '';


function sendRequest(url, method, data) {
    url = SERVER_NAME + url;
    var request = new XMLHttpRequest();
    request.open(method, url, true);
    request.withCredentials = true;
    request.send(objectToQueryString(data));
}

function objectToQueryString(data) {
    return isObject(data) ? getQueryString(data) : data;
}

function isObject(data) {
    return Object.prototype.toString.call(data) === '[object Object]';
}

function getQueryString(object) {
    return Object.keys(object).reduce(function (acc, item) {
        var prefix = !acc ? '' : acc + '&';
        return prefix + encode(item) + '=' + encode(object[item]);
    }, '')
}

function encode(value) {
    return encodeURIComponent(value);
}

function sendVisit(page) {
    sendRequest('tracker/visit', 'GET', {
        page: page
    });
}

function sendEvent(name, value) {
    sendRequest('tracker/action', 'POST', {
        type: 'event',
        name: name,
        value: value
    });
}

function sendData(name, value) {
    sendRequest('tracker/action', 'POST', {
        type: 'data',
        name: name,
        value: value
    });
}

function sendContact(name, value) {
    sendRequest('tracker/action', 'POST', {
        type: 'contact',
        name: name,
        value: value
    });
}

module.exports = function (serverName) {
    SERVER_NAME = serverName;

    return {
        sendVisit: sendVisit,
        sendEvent: sendEvent,
        sendData: sendData,
        sendContact: sendContact
    };
};
