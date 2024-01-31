from tkinter import Image

from django.shortcuts import render

# Create your views here.

from culapp import models
from django.http import JsonResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from PIL import Image
import os

def HebeiClapperOpera(request):
    return render(request, 'works_detail/HebeiClapperOpera.html')

def HengshuiInteriorPainting(request):
    return render(request, 'works_detail/HengshuiInteriorPainting.html')

def LaotingClayFigure(request):
    return render(request, 'works_detail/LaotingClayFigure.html')

def PekingOpera(request):
    return render(request, 'works_detail/PekingOpEra.html')

def ShadowPuppets(request):
    return render(request, 'works_detail/ShadowPuppets.html')

def WuqiaoAcrobatics(request):
    return render(request, 'works_detail/WuqiaoAcrobatics.html')