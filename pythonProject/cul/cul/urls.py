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
# import cul.culapp.views as views

urlpatterns = [
    path('base', index.base ),
    # 首页
    path('', index.index ),
    path('logged', index.logged ),
    path('get_number', index.get_number),
    # 非遗代表作名录部分 MasterPieces ----------------------------
    path('get_masterpieces', index.get_masterpieces),
    path('get_detailurl_masterpieces', index.get_detailurl_masterpieces),
    path('get_detailurl_craftsman', index.get_detailurl_craftsman),
    # 手工艺者部分 ------------------------------------
    path('get_craftsman', index.get_craftsman),
    path('get_craftsman_img', index.get_craftsman_img),
    # 代表作名录详情 ------------------------------------
    path('works_detail/HebeiClapperOpera', works_detail.HebeiClapperOpera ),
    path('works_detail/HengshuiInteriorPainting', works_detail.HengshuiInteriorPainting ),
    path('works_detail/LaotingClayFigure', works_detail.LaotingClayFigure),
    path('works_detail/PekingOpera', works_detail.PekingOpera),
    path('works_detail/ShadowPuppets', works_detail.ShadowPuppets),
    path('works_detail/WuqiaoAcrobatics', works_detail.WuqiaoAcrobatics),

    # 手工艺者详情 ------------------------------------
    path('craftsman_detail/LiuJunYing', craftsman_detail.LiuJunYing ),

    path('admin/', admin.site.urls)
]
