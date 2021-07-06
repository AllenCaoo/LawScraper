
const formdata = (ev)=>{
    ev.preventDefault();
    var first = document.getElementById("firstname").value.replace(/\s/g, "");
    var last = document.getElementById("lastname").value.replace(/\s/g, "");
    var email = document.getElementById("email").value.replace(/\s/g, "");
    //let exists = check(email, function(err, res) {
    //    console.log('res: '+res);
    //});
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


function saveInfo(name, email) {
    let fileName = "backend/.info/subs.JSON";
    /*
    fetch(new Request(fileName))
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            console.log(data);
        });
    var dict = {};
    */
    var dict = JSON.parse(localStorage.getItem("nameToEmails")) || JSON.parse("{ }");
    dict[name] = email;
    var newData = JSON.stringify(dict);
    localStorage.setItem('nameToEmails', newData);
}

document.addEventListener('DOMContentLoaded', () =>{
    document.getElementById('submit button').addEventListener('click', formdata);
})

window.formdata = formdata;
window.validateEmail = validateEmail;
window.saveInfo = saveInfo;