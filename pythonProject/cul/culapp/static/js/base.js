// 页面加载时，得到时间
$(window).load(function(){
    timeText()
    logged()
});

// 实时更新时间
setInterval(timeText,100)

//获取当前时间
function timeText(){
    var date =  new Date();

    year = date.getFullYear();
    month = date.getMonth() + 1;
    day = date.getDate();
    hours = date.getHours();
    minutes = date.getMinutes();
    seconds = date.getSeconds();
    console.log(year, month, day);

    $('#time').text(
        year + '年' + month + '月' + day + '日   ' 
    +  (hours < 10 ? '0' + hours : hours) 
    + ":" 
    + (minutes < 10 ?  '0' + minutes : minutes) 
    + ":" 
    + (seconds < 10 ? '0' + seconds : seconds)
    )
};

// 判断是否登录
function logged(){
    console.log('logged')
    $.ajax(
        {
            url:'../logged',
            type:'get',
            success:function(response){
                console.log('logged-response:', response.username)
                if(response.username != null){
                    $('#login').append(
                        '<a href="#" id="login">'
                        +   response.username
                        + '</a>'
                    )
                    if(response.username == '传承人xxx'){
                        $('.m2').append(
                            '<li>'
                            +   '<a href="../chat/craftsman">'
                            +       '手工艺者'
                            +   '</a>'
                            + '</li>'
                        )
                    }
                }
                else{
                    $('#login').append(
                        '<a href="../login" onclick="click_login()" id="login">'
                        +   '登录'
                        + '</a>'
                    )
                }
            }

    }
    )     
}

