
// window.onload=name_line_height()
//获取手工艺者的信息
$(window).load(function(){
    get_craftsman()
    get_masterpieces()
    // craftsman_img
});

// 分别获取 代表作名录、手工艺者的数量
var num_pieces = get_number('MasterPieces') ;
var num_craftsman = get_number('Craftsman') ;
console.log('num_pieces', num_pieces)
console.log('num_craftsman', num_craftsman)

var cot_pieces = 0;     //设置一个计数器，初始值为0；作用是用来监听点击切换的时候哪一个图片应该隐藏或者显示
var cot_craftsman = 0;

// 代表作名录的按钮
function next_pieces(){  
 if(cot_pieces < num_pieces-1 ){    
  $('.subwork').eq(cot_pieces).animate({'margin-left':'-420px'}, 500);    
  cot_pieces++;
//   console.log('cot_pieces:', cot_pieces)
 }
}
function prev_pieces(){  
 if(cot_pieces > 0){    
  cot_pieces--;    
  $('.subwork').eq(cot_pieces).animate({'margin-left':'40px'}, 500);
//   console.log('cot_pieces:', cot_pieces)
 }
}

// 手工艺者的按钮
function next_craftsman(){  
    if(cot_craftsman < num_craftsman - 1){    
     $('.subname').eq(cot_craftsman).animate({'margin-left':'-90px'}, 500);    
     cot_craftsman++;
    }
   }
function prev_craftsman(){  
    if(cot_craftsman > 0 ){    
     cot_craftsman--;    
     $('.subname').eq(cot_craftsman).animate({'margin-left':'0px'}, 500);
    }
   }

// 获取元素个数（非遗项目、手工艺者、展览与活动）
// 查某表元素的个数
function get_number( table ){
    var num = 0
    // console.log( "get_number")
    // console.log(table)
    $.ajax(
        {
        url:"get_number",
        type:'post',  // 不指定默认就是get，都是小写
        data: { table
                }, 
        headers: {"X-CSRFToken": $.cookie('csrftoken')},
        async : false,

        success:function (response) {
            // console.log('response', response.num)
            num = response.num
            // console.log('num', num)
            }
        }
    )
    return num
}


//    代表作名录 ————————————————————————————————————————————————
// 获取代表作名录信息
function get_masterpieces(){
    n = 0
    console.log( "get_masterpieces/")
    $.ajax(
    {
        url:'get_masterpieces',
        type:'get',
        success:function(response){
            $(".cont1 .work").empty(); 
            console.log("get_masterpieces" + response)
            $.each(response.masterpieces, function(key, value) {
                console.log('reponse.value:', value)
                $('.cont1 .work').append(
                    '<div class="subwork"  onclick="click_masterpieces(this)"> '
                    + '<div class="color"></div>'
                    + '<div class="img">'
                    +     '<img src=" '
                    +       value.img_path
                    +       '">'
                    + '</div>'
                    + '<div class="txt"> '
                    + value.pieces_name_ch
                    + '</div>'
                + '</div>'
                )
            })        
        }
    }
    )       
}

function get_masterpieces_img(){
    var   name = this1.innerText; 
    // console.log('name', name);
    // 更换图片
    $.ajax(
        {
        url:"get_craftsman_img",
        type:'post',  // 不指定默认就是get，都是小写
        data: { name
        }, 
        headers: {"X-CSRFToken": $.cookie('csrftoken')},
        async : false,

        success:function (response) {
            // console.log('response', response.craftsman_img_path)
            $('.cont2 .img img').attr('src', "static/" + response.craftsman_img_path )
            }
        }
    )
}

// 点击进入详情页
function click_masterpieces(this1){
    var name = this1.innerText
    console.log('name:', name)
    $.ajax(
        {
            url:'get_detailurl_masterpieces',
            type:'post',
            data:{
                name
            },
            headers:{"X-CSRFToken": $.cookie('csrftoken')},
            async: false,
            success:function(response){
                var url = response.url
                console.log(response.url)
                location.href = url
            }

        }
    )
}


//    手工艺者部分 ————————————————————————————————————————————————

//生成从minNum到maxNum的随机数
function randomNum(minNum,maxNum){ 
    // var result = Math.random()*(maxNum  -minNum + 1) + minNum;
    // while(result == minNum) {
    //     result = Math.random()*(maxNum - minNum + 1) + minNum;
    // }

    var result = Math.floor(Math.random()*(maxNum - minNum + 1)) + minNum;

    return result; 
} 

// 获取随机高度
function name_line_height(){
    // console.log($('.man').height())
    var hei = $('.man').height();
    // var hei = document.getElementsByClassName(".cont2 .man").getAttribute("height"); 
    var hei_m = $('.cont2 .name').height();
    if(hei_m == null){
        return 400
    }
    // var hei_m = document.getElementsByClassName('.cont2 .line').clientHeight;
    var rand = randomNum( hei_m + 100, hei - 100 );
    // console.log(hei_m, hei)
    // console.log(hei_m + 100, hei - hei_m-100 , rand)
    
    return rand
}


// 获取手工艺者的信息
// class Craftsman(models.Model):
//     craftsman_id = models.IntegerField(null=False, primary_key=True, verbose_name='craftsman_id')
//     craftsman_name = models.CharField(max_length=64, null=False, verbose_name='姓名')
//     item = models.ForeignKey(MasterPieces, on_delete=models.DO_NOTHING, verbose_name='传承项目')
function get_craftsman(){
    // console.log( "get_craftsman/")
    $.ajax(
    {
        url:'get_craftsman',
        type:'get',
        success:function(response){
            $(".man_name").empty(); 
            // console.log("get_craftsman:" + response)
            $.each(response.craftsman, function(key, value) {
                console.log('value:', value)
                $('.man_name').append(
                    ' <div class="subname fl" onmouseover="over(this)" onclick="click_craftsman(this)"> '
                    +    '<div class="line"></div>'
                    +    '<div class="name" style=" margin-top: -' + name_line_height() + 'px; "> '
                    +       value.item      // 皮影
                    +       '：'
                    +       value.craftsman_name_ch        // 王彪
                    +       '</div>'
                    + '</div>'
                )
            })            
        }
    }
    )       
}

// 鼠标悬停时，更换为对应图片
function over(this1){
    var   name = this1.innerText; 
    // console.log('name', name);
    // 更换图片
    $.ajax(
        {
        url:"get_craftsman_img",
        type:'post',  // 不指定默认就是get，都是小写
        data: { name
                }, 
        headers: {"X-CSRFToken": $.cookie('csrftoken')},
        async : false,

        success:function (response) {
            // console.log('response', response.craftsman_img_path)
            $('.cont2 .img img').attr('src', "static/" + response.craftsman_img_path )
            }
        }
    )
}

function click_craftsman(this1){
    var name = this1.innerText
    console.log('get_detailurl_craftsman name:', name)
    $.ajax(
        {
            url:'get_detailurl_craftsman',
            type:'post',
            data:{
                name
            },
            headers:{"X-CSRFToken": $.cookie('csrftoken')},
            async: false,
            success:function(response){
                var url = response.url
                console.log(response.url)
                location.href = url
            }

        }
    )
}

