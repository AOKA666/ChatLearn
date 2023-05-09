$(document).ready(function() {
    // 监听textarea的输入事件
    $("#input").on("input", function() {
        var message = $(this).val();
        // 如果textarea内部有数据，激活“发送”按钮
        if ($.trim(message) !== "") {
          $("#btn-send").prop("disabled", false);
        }else{
            $("#btn-send").prop("disabled", true);
        }
      });
    $("#btn-restart").click(function() {
        location.reload();
      });
    // 添加消息的函数
    function add_msg(role, msg){
        // 创建聊天框，并添加到聊天框容器中
        var chatContainer = $('.chat-container');
        var chatBox = $('<div>').addClass('chat-box');
        if(role=='user'){
            chatBox.addClass('pull-right');
        }
        chatContainer.append(chatBox);

        // 创建消息元素，并添加到聊天框中
        
        var message = $('<div>').addClass('message');
        var message_area = $('<div>').addClass('message-area');
        message_area.append(message);
        chatBox.append(message_area);

        // 创建头像元素，并添加到聊天框中
        var avatar = $('<div>').addClass('avatar');        
        if(role =='ai'){
            avatar.css('background-image', "url('static/img/avatar.png')");
            // chatBox.append(avatar);
            // 将头像元素复制一份，并添加到消息区域前面
            avatar.insertBefore(chatBox.find('.message-area'));
        }else{
            avatar.css('background-image', "url('static/img/user.png')");
            // chatBox.append(avatar);
            // 将头像元素添加到消息区域后面，并设置消息区域样式
            avatar.insertAfter(chatBox.find('.message-area'));
        }
        var p = $('<p>').text(msg);
        message.append(p);         
    }
    // 更新ai的对话框
    function update_ai_msg(msg){
        $('.chat-box:last-child p').text("");
        var div = $(".chat-box:last-child .message");
        for (var i = 0; i < msg.length; i++) {
            var p = $('<p>').text(msg[i]);
            div.append(p);
        }  
    }
        
    function send_msg(messageText, status){
        fetch('/send', {
            method: 'POST',
            body: JSON.stringify({ message: messageText }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            // 更新页面上的 message-area 元素
            console.log(data.response);
            update_ai_msg(data.response)
            if(status=='start'){
                start();
            }else{
                over();
            }
        })
        .catch(err => console.error(err));
    }
    // 后端返回之后的两种做法
    function start(){
        
        // $("#btn-send").prop("disabled", false);
        $("#input").prop("disabled", false).focus();
    }
    function over(){
        // $("#btn-start").prop("disabled", true);
        
        $("#input").prop("disabled", true);
        $("#btn-restart").prop("disabled", false);
    }

    // 当用户在表单中输入消息并提交时执行以下代码
    $('#message-form').submit(function(event) {
        // 防止表单默认提交行为
        event.preventDefault();
        // 获取用户输入的消息文本并清空输入框
        var messageText;
        if($("#btn-send").is(":disabled")){
            messageText = '开始练习';
            add_msg('user', messageText);
            add_msg('ai', '请稍候...');
            // 禁用“开始练习”按钮
            $("#btn-start").prop("disabled", true);            
            send_msg(messageText, 'start');
        }else{
            messageText = $("#input").val();
            add_msg('user', messageText);
            $("#input").prop("disabled", true);
            add_msg('ai', '请稍候...');
            $("#btn-send").prop("disabled", true);
            $("#input").val("");
            send_msg(messageText, 'over');
            
        }
        
    });
   
})