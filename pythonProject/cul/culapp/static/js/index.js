var cot=0;//设置一个计数器，初始值为0；作用是用来监听点击切换的时候哪一个图片应该隐藏或者显示
function next(){  
 if(cot<=2){    
  $('.subwork').eq(cot).animate({'margin-left':'-420px'}, 500);    
  cot++;
 }
}
function prev(){  
 if(cot>0){    
  cot--;    
  $('.subwork').eq(cot).animate({'margin-left':'40px'}, 500);
 }
}

//生成从minNum到maxNum的随机数
function randomNum(minNum,maxNum){ 
    // var result = Math.random()*(maxNum  -minNum + 1) + minNum;
    // while(result == minNum) {
    //     result = Math.random()*(maxNum - minNum + 1) + minNum;
    // }

    var result = Math.floor(Math.random()*(maxNum - minNum + 1)) + minNum;

    return result; 
} 

function name_line_height(){
    console.log($('.man').height())
    var hei = $('.man').height();
    // var hei = document.getElementsByClassName(".cont2 .man").getAttribute("height"); 
    var hei_m = $('.cont2 .name').height();
    // var hei_m = document.getElementsByClassName('.cont2 .line').clientHeight;
    var rand = randomNum( hei_m + 100, hei - hei_m-100 );
    
    console.log(hei_m + 100, hei - 100)
    console.log( hei, hei_m, rand);
    $('.name').attr("style", 'margin-top: -' + rand + 'px' );
    console.log($('.name').attr("margin-top"));
}

window.onload=name_line_height()