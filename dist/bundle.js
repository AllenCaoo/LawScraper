(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){

},{}],2:[function(require,module,exports){
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
},{"fs":1}]},{},[2]);
