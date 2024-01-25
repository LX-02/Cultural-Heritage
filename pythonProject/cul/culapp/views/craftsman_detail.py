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