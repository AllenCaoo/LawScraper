const fs = require('fs');

const formdata = (name, email)=>{
    // ev.preventDefault();
    if (first && last && email && validateEmail(email)) {
        alert("You have subscribed");
        saveInfo(first + " " + last, email);
        document.forms[0].reset(); // reset form
    }
}

function validateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

module.exports = {formdata, validateEmail};