
    prev = 0

    var example = {{ json_laugh }};
    var roomName = {{ room_name_json }};

    var chatSocket = new WebSocket(
        'ws://' + window.location.host +
        '/ws/chat/' + roomName + '/');

    chatSocket.onmessage = function(e) {
        var data = JSON.parse(e.data);
        var message = data['message'];
        document.querySelector('#customer-chat').value = (message + '\n');
    };

    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    document.querySelector('#chat-next').focus();
    document.querySelector('#chat-next').onkeyup = function(e) {
        if (e.keyCode === 13) {  // enter, return
            document.querySelector('#chat-submit-next').click();
        }
    };

    document.querySelector('#chat-submit-next').onclick = function(e) {
        prev += 1;
        var messagePreviousDom = document.querySelector('#chat-previous');
        messagePreviousDom.value = example[prev-1].song;
        var messageChatDom = document.querySelector('#chat');
        messageChatDom.value = example[prev].song;
        var messageNextDom = document.querySelector('#chat-next');
        messageNextDom.value = example[prev+1].song;
        var messageCustomerChatDom = document.querySelector('#chat');
        var message = messageCustomerChatDom.value;
        chatSocket.send(JSON.stringify({
            'message': message,
        }));
    };

    document.querySelector('#chat-submit-previous').onclick = function(e) {
        prev -= 1;
        var messagePreviousDom = document.querySelector('#chat-previous');
        messagePreviousDom.value = example[prev-1].song;
        var messageChatDom = document.querySelector('#chat');
        messageChatDom.value = example[prev].song;
        var messageNextDom = document.querySelector('#chat-next');
        messageNextDom.value = example[prev+1].song;
        var messageCustomerChatDom = document.querySelector('#chat');
        var message = messageCustomerChatDom.value;
        chatSocket.send(JSON.stringify({
            'message': message,
        }));
    };

    /*
    해결해야 할 이슈
        chat에서 전달할 때 처음에 모든 칸을 비워주는 역할을 하는 함수가 필요.
        onclick에서 작성할 것이 아니라, 메세지를 받는 시점에서 작성해야 함.
        messagePreviousDom.value = '';
        messageChatDom.value = '';
        messageNextDom.value = '';
    */