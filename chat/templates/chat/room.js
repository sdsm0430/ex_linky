var roomName = {{ room_name_json }};

    /*
       WebSocket 뒤에는 url
       JSON은 주로 웹서버와의 데이터를 교환할 때 쓰인다.
       JSON.parse 란 string 객체를 JSON 객체로 변환시켜준다.
       The onmessage property of the WindowEventHandlers is the EventHandler called whenever
       an object receives a message event.
    */
    var chatSocket = new WebSocket(
        'ws://' + window.location.host +
        '/ws/chat/' + roomName + '/');

    chatSocket.onmessage = function(e) {
        var data = JSON.parse(e.data);
        var message = data['message'];
        document.querySelector('#chat-log').value += (message + '\n');
    };

    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    document.querySelector('#chat-message-input').focus();

    /*
       onkeyup : 자판에서 키를 눌렀다 놓았을 때 발생하는 이벤트
       onkeypress : 자판에서 키를 누르고 있는 동안 발생하는 이벤트
       onkeydown : 자판에서 키를 눌렀을 때 발생하는 이벤트
       keycode : 말 그대로 키 코드, ENTER가 13이다.
       function의 e는 event를 뜻한다.
       onclick : 마우스의 click 이벤트 발생을 의미
       JSON.stringify 란 JSON 객체를 String 객체로 변환시켜준다.
    */

    document.querySelector('#chat-message-input').onkeyup = function(e) {
        if (e.keyCode === 13) {  // enter, return
            document.querySelector('#chat-message-submit').click();
        }
    };

    document.querySelector('#chat-message-submit').onclick = function(e) {
        var messageInputDom = document.querySelector('#chat-message-input');
        var message = messageInputDom.value;
        chatSocket.send(JSON.stringify({
            'message': message
        }));

        messageInputDom.value = '';
    };