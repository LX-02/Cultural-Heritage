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
    $.ajax(
        {
            url:'logged',
            type:'get',
            success:function(response){
                console.log(response)
                if(response.username != null){
                    $('#login').text(response.username)
                }
                else{
                    $('#login').text('登录')
                }
            }

    }
    )
    $.ajax(
        {
            url:'get_craftsman',
            type:'get',
            success:function(response){
                        
            }
        }
        )      
}
