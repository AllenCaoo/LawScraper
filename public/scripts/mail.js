const fs = require('fs');

const formdata = (name, email) => {
    // ev.preventDefault();
    if (first && last && email && validateEmail(email)) {
        saveInfo(first + " " + last, email);
        return true;
    }
    return false;
}

function validateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

function saveInfo(name, email) {
    // TODO: save info to subs.JSON
}

module.exports = {formdata, validateEmail, saveInfo};