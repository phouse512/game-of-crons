var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var bodyParser = require('body-parser');
var contributions = {};

app.use(bodyParser());
app.use(express.static('public'));

app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

app.post('/update_map', function(req, res) {
    console.log(req.body);
    io.sockets.emit('update', {data: req.body });
    res.send("hi");
});

io.on('connection', function(socket) {
    console.log('YEAHHH')
    socket.emit('news', { hello: 'world' });
    socket.on('my other event', function(data) {
        console.log(data);
    });
});


http.listen(3000, function() {
    console.log('listening on localhost:3000');
});
