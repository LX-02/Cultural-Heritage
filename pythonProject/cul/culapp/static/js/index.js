var cot=0;//设置一个计数器，初始值为0；作用是用来监听点击切换的时候哪一个图片应该隐藏或者显示
function next(){  
 if(cot<=2){    
  $('.subwork').eq(cot).animate({'margin-left':'-420px'},500);    
  cot++;
 }
}
function prev(){  
 if(cot>0){    
  cot--;    
  $('.subwork').eq(cot).animate({'margin-left':'40px'},500);
 }
}