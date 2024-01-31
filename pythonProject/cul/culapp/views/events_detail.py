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

def event1(request):
    return render(request, 'events_detail/event1.html')

def event2(request):
    return render(request, 'events_detail/event2.html')

def event3(request):
    return render(request, 'events_detail/event3.html')

def event4(request):
    return render(request, 'events_detail/event4.html')

def event5(request):
    return render(request, 'events_detail/event5.html')

def event6(request):
    return render(request, 'events_detail/event6.html')

def event7(request):
    return render(request, 'events_detail/event7.html')
