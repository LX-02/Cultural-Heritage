from tkinter import Image

from django.shortcuts import render

# Create your views here.

from culapp import models
from django.http import JsonResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from PIL import Image
import os

def LiuJunYing(request):
    return render(request, 'craftsman_detail/LiuJunYing.html')

def ZhaoYuMing(request):
    return render(request, 'craftsman_detail/ZhaoYuMing.html')

def DongZhuangZhuang(request):
    return render(request, 'craftsman_detail/DongZhuangZhuang.html')

def WangZiYong(request):
    return render(request, 'craftsman_detail/WangZiYong.html')

def ZhanYueFeng(request):
    return render(request, 'craftsman_detail/ZhanYueFeng.html')

def ZhuShaoYu(request):
    return render(request, 'craftsman_detail/ZhuShaoYu.html')

def ZhangYouLin(request):
    return render(request, 'craftsman_detail/ZhangYouLin.html')

def WangBiao(request):
    return render(request, 'craftsman_detail/WangBiao.html')

def WangHaiYan(request):
    return render(request, 'craftsman_detail/WangHaiYan.html')

def WangBaoHe(request):
    return render(request, 'craftsman_detail/WangBaoHe.html')