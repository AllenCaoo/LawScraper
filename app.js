// imports 
const http = require('http');
const fs = require('fs');
const express = require('express');
const app = express();
const port = 3000;

app.use(express.static(__dirname+'/public'));
app.use('/images', express.static(__dirname + 'public/images'));
app.use('/scripts', express.static(__dirname + 'public/scripts'));


const server = http.createServer(function(req, res) {
    res.writeHead(200, { 'Content-Type': "text/html" });
    fs.readFile('views/index.html', function(error, data) {
        if (error) {
            res.writeHead(404);
            res.write('Error: File not found');
        } else {
            res.write(data);
        }
        res.end();
    })
})

// listen on port
server.listen(port, function(error) {
    if (error) {
        console.log("errored");
    } else {
        console.log("listening...");
    }
})