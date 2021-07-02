var fs = require('fs');

function formdata() {
    var first = document.getElementById("firstname").value.toLowerCase().replace(/\s/g, "");
    var last = document.getElementById("lastname").value.toLowerCase().replace(/\s/g, "");
    var email = document.getElementById("email").value.toLowerCase().replace(/\s/g, "");
    //let exists = check(email, function(err, res) {
    //    console.log('res: '+res);
    //});
    if (first && last && email && validateEmail(email)) {
        alert("You have subscribed");
        saveInfo()
    }

}

function validateEmail(email) {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

function saveInfo() {
    
}