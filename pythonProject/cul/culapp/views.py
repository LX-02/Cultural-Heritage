from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def HebeiClapperOpera(request):
    return render(request, 'works_detail/HebeiClapperOpera.html')

def LaotingClayFigure(request):
    return render(request, 'works_detail/LaotingClayFigure.html')