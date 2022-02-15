window.onload = function() {
 
    var messages = [];
    var socket = io.connect('http://192.168.1.3:3700');
    var field = document.getElementById("field");
    var sendButton = document.getElementById("send");
    var content = document.getElementById("content");
    var name = document.getElementById("name");
 
    socket.on('message', function (data) {
        if(data.message) {
            messages.push(data);
            var html = '';
            for(var i=0; i<messages.length; i++) {
                //html += messages[i] + '<br />';
                html += '<b>' + (messages[i].username ? messages[i].username : 'Server') + ': </b>';
                html += messages[i].message + '<br />';
            }
            content.innerHTML = html;
            content.scrollTop = content.scrollHeight;
        } else {
            console.log("There is a problem:", data);
        }
    });
 
    sendButton.onclick = sendMessage = function() {
        //var text = field.value;
        //alert(text);
        //socket.emit('send', { message: text });
        if(name.value == "") {
            alert("Please type your name!");
        } else {
            var text = field.value;
            socket.emit('send', { message: text, username: name.value });
            field.value = "";
        }
    };
 
}

$(document).ready(function() {
    $("#field").keyup(function(e) {
        if(e.keyCode == 13) {
            sendMessage();
        }
    });
    $("#content").scrollTop($("#content")[0].scrollHeight);
});


function notifyTyping() {
  //var user = $('#user').val();
  //socket.emit('send', username);
  //alert();
}