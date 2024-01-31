from tkinter import Image

from django.shortcuts import render
from culapp.models import Message

from django.http import HttpResponse
# Create your views here.

from culapp import models
from django.http import JsonResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from PIL import Image
import os

def chat_craftsman(request):
    return render(request, 'chat/craftsman.html')

def chat_masses(request):
    return render(request, 'chat/masses.html')

def chat_message(request):
    return render(request, 'chat/message.html')

# 提交表单
def post_content(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        partment = request.POST.get('partment','')
        message = request.POST.get('message', '')
        # 实例化对象
        o_message = Message()
        o_message.name = name
        o_message.email = email
        o_message.partment = partment
        o_message.text = message
        # 调用save方法保存数据
        o_message.save()
        return render(request, 'chat/message.html', {'post_result':'提交成功'})
    else:
        return render(request, 'chat/message.html')