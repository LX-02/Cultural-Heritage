from django.shortcuts import render

# Create your views here.

from culapp import models
from django.http import JsonResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
# from PIL import Image
import os

def index(request):
    print('index ok')
    return render(request, 'index.html')

# 获取元素的个数（用于非遗项目、手工艺者、活动）
def get_number(request):
    print('get_number:::::::::::::::::???????????')
    if request.method == 'GET':
        print('!!!!!!!!!!!!!11!!!111111111111111111111111111')
    if request.method == "POST":
        print('POST')
        table = request.POST.get('table', False)
        if table == 'MasterPieces':
            list = models.MasterPieces.objects.all()
        elif table == 'Craftsman' :
            list = models.Craftsman.objects.all()
        elif table == 'Events':
            list = models.Events.objects.all()
        else:
            list = models.User.objects.all()
        # list = models.MasterPieces.objects.all()
        lis = []
        for value in list:
            lis.append( model_to_dict(value) )
        num = len(lis)
        print(lis)
        print('table:', table, 'num:', num)
        return JsonResponse({'num': num})

# 非遗代表作名录部分 MasterPieces


# 手工艺者部分

# 获取手工艺者的信息
def get_craftsman(request):
    print('get_craftsman()')
    craftsman_list = models.Craftsman.objects.all()
    print(craftsman_list)
    craftsman = []
    for value in craftsman_list:
        dic = {}
        # print('type', type(model_to_dict(value)))
        dic = model_to_dict(value)
        dic['item'] = get_pieces_name(model_to_dict(value)['item'])
        craftsman.append(dic)
        print('dic:', dic)
        # get_pieces_name(model_to_dict(value)['item'])

    # print('craftsman:',craftsman)
    return JsonResponse({'craftsman':craftsman})


# 根据item查询非遗项目名称
def get_pieces_name(item):
    pieces = models.MasterPieces.objects.filter(pieces_id = item)
    for value in pieces:
        pieces_name = model_to_dict(value)['pieces_name']
    print('name:', pieces_name)
    return pieces_name


# 根据


# 判断图片是横版还是竖版
# def if_horizon(src):
    # img = Image.open(src)
    # w,h = img.size
    # if w >= h:
    #     return  True
    # return  False



def HebeiClapperOpera(request):
    return render(request, 'works_detail/HebeiClapperOpera.html')

def LaotingClayFigure(request):
    return render(request, 'works_detail/LaotingClayFigure.html')