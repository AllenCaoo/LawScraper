const mail = require('./public/scripts/mail')
const express = require('express');
const path = require('path');
var bodyParser = require('body-parser'); 

const app = express();

// Set static folder
app.use(express.static(path.join(__dirname, 'public')));

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
  }));

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => console.log(`Server started on port ${PORT}`));

app.post('/views/index.html', function(req, res) {
    res.sendStatus(200);
    first = req.body.firstname;
    last = req.body.lastname;
    email = req.body.email;
    mail.formdata(first + ' ' + last, req.body.email);
    console.log(first + ' ' + last + ' has joined.');
});


