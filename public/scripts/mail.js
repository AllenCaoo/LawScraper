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
    path = 'public/src/subs.JSON';
    var prevData = fs.readFileSync(path);
    var prevDataObj = JSON.parse(prevData);
    prevDataObj[name] = email;
    var newData  = JSON.stringify(prevDataObj);
    fs.writeFile(path, newData, err => {
        if(err) throw err;
        console.log("New data added");
    });   
}

module.exports = {formdata, validateEmail, saveInfo};