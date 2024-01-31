"""cul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# from cul.culapp.views import index
# import culapp.views as views
from culapp.views import index
from culapp.views import works_detail
from culapp.views import craftsman_detail
from culapp.views import chat
from culapp.views import events_detail
# import cul.culapp.views as views

urlpatterns = [
    path('base', index.base ),
    # 首页
    path('', index.index, name='index' ),
    path('login', index.login, name='login'),
    path('logged', index.logged, name='logged' ),
    path('get_number', index.get_number, name='get_number'),
    # 非遗代表作名录部分 MasterPieces ----------------------------
    path('get_masterpieces', index.get_masterpieces, name='get_masterpieces'),
    path('get_detailurl_masterpieces', index.get_detailurl_masterpieces, name='get_detailurl_masterpieces'),
    path('get_detailurl_craftsman', index.get_detailurl_craftsman, name='get_detailurl_craftsman'),
    # 手工艺者部分 ------------------------------------
    path('get_craftsman', index.get_craftsman, name='get_craftsman'),
    path('get_craftsman_img', index.get_craftsman_img, name='get_craftsman_img'),
    # 代表作名录详情 ------------------------------------
    path('works_detail/HebeiClapperOpera', works_detail.HebeiClapperOpera, name='works_detail/HebeiClapperOpera' ),
    path('works_detail/HengshuiInteriorPainting', works_detail.HengshuiInteriorPainting, name='works_detail/HengshuiInteriorPainting' ),
    path('works_detail/LaotingClayFigure', works_detail.LaotingClayFigure, name='works_detail/LaotingClayFigure'),
    path('works_detail/PekingOpera', works_detail.PekingOpera, name='works_detail/PekingOpera'),
    path('works_detail/ShadowPuppets', works_detail.ShadowPuppets, name='works_detail/ShadowPuppets'),
    path('works_detail/WuqiaoAcrobatics', works_detail.WuqiaoAcrobatics, name='works_detail/WuqiaoAcrobatics'),
    # 手工艺者详情 ------------------------------------
    path('craftsman_detail/LiuJunYing', craftsman_detail.LiuJunYing, name='craftsman_detail/LiuJunYing' ),
    path('craftsman_detail/ZhaoYuMing', craftsman_detail.ZhaoYuMing, name='craftsman_detail/ZhaoYuMing' ),
    path('craftsman_detail/DongZhuangZhuang', craftsman_detail.DongZhuangZhuang, name='craftsman_detail/DongZhuangZhuang'),
    path('craftsman_detail/WangZiYong', craftsman_detail.WangZiYong, name='craftsman_detail/WangZiYong'),
    path('craftsman_detail/ZhanYueFeng', craftsman_detail.ZhanYueFeng, name='craftsman_detail/ZhanYueFeng'),
    path('craftsman_detail/ZhuShaoYu', craftsman_detail.ZhuShaoYu, name='craftsman_detail/ZhuShaoYu'),
    path('craftsman_detail/ZhangYouLin', craftsman_detail.ZhangYouLin, name='craftsman_detail/ZhangYouLin'),
    path('craftsman_detail/WangBiao', craftsman_detail.WangBiao, name='craftsman_detail/WangBiao'),
    path('craftsman_detail/WangHaiYan', craftsman_detail.WangHaiYan, name='craftsman_detail/WangHaiYan'),
    path('craftsman_detail/WangBaoHe', craftsman_detail.WangBaoHe, name='craftsman_detail/WangBaoHe'),
    # events 活动 ------------------------------------
    path('events_detail/event1', events_detail.event1, name='events_detail/event1' ),
    path('events_detail/event2', events_detail.event2, name='events_detail/event2'),
    path('events_detail/event3', events_detail.event3, name='events_detail/event3'),
    path('events_detail/event4', events_detail.event4, name='events_detail/event4'),
    path('events_detail/event5', events_detail.event5, name='events_detail/event5'),
    path('events_detail/event6', events_detail.event6, name='events_detail/event6'),
    path('events_detail/event7', events_detail.event7, name='events_detail/event7'),
    # chat 交流沟通、留言 ------------------------------------
    path('chat/craftsman', chat.chat_craftsman, name='chat/craftsman'),
    path('chat/masses', chat.chat_masses, name='chat/masses'),
    path('chat/message', chat.chat_message, name='chat/message'),
    path('chat/message/post_content', chat.post_content, name='chat/message/post_content'),

    path('admin/', admin.site.urls)
]
