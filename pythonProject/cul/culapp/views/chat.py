from tkinter import Image

from django.shortcuts import render

# Create your views here.

from culapp import models
from django.http import JsonResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from PIL import Image
import os

def chat_craftsman(request):
    return render(request, 'chat/craftsman.html')