const roomName = JSON.parse(document.getElementById('room-name').textContent);

const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + roomName
    + '/'
);

chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
//    console.log(data)
//    console.log(data.sumroll)
    if(data.sumroll == 0)
    {
        document.querySelector('#chat-log').innerHTML += `
        <div class='message'>
            <div class="spacer"></div>
            <div class='avatar' aria-hidden="true">
                <img src=`+data.avatar+`>
            </div>
            <span class='by'>`+data.name+`: </span>`+
            data.message+`
        </div>`
        document.getElementsByClassName('textchatcontainer')[0].scrollTo(0,document.getElementsByClassName('textchatcontainer')[0].scrollHeight)
    }
    else
    {
        document.querySelector('#chat-log').innerHTML += `
        <div class='message'>
            <div class="spacer"></div>
            <div class='avatar' aria-hidden="true">
                <img src=`+data.avatar+`>
            </div>
            <span class='by'>`+data.name+`: </span>
            <div class="formula">Бросает `+data.message+`</div>
            <div class="formula formattedformula">`+data.rolls+`</div>
            <div class="rolled">=`+data.sumroll+`</div>
        </div>`
        document.getElementsByClassName('textchatcontainer')[0].scrollTo(0,document.getElementsByClassName('textchatcontainer')[0].scrollHeight)
    }
};

chatSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
};

document.getElementsByClassName('textchatcontainer')[0].scrollTo(0,document.getElementsByClassName('textchatcontainer')[0].scrollHeight)
document.querySelector('#chat-message-input').focus();
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message
    }));
    messageInputDom.value = '';
};
