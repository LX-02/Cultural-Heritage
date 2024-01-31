from tkinter import Image

from django.shortcuts import render

# Create your views here.

from culapp import models
from django.http import JsonResponse, HttpResponseRedirect
from django.forms.models import model_to_dict
from PIL import Image
import os

def base(request):
    print('base ok')
    return render(request, 'base.html')

def login(request):
    return render(request, 'login.html')

def index(request):
    if request.method == 'POST':
        print('LOGIN.POST:')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = models.User.objects.filter(username=username)
        # if username == '' or password == '':
        #     return
        if user:
            if user.first().password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.first().user_id
                request.session['username'] = user.first().username
                # request.session['position_choice'] = user.first().position
                request.session['position'] = user.first().get_position_display()
                # request.session['workspace'] = user.first().workspace
                return render(request,'index.html')
    # return render(request, 'login.html')
    return render(request, 'index.html')

def logged(request):
    username = request.session.get('username')
    # if request.user.is_authenticated:
    #     username = request.user.username
    # else:
    #     username = None
    print('username:', username)
    return JsonResponse({'username':username})


# 获取元素的个数（用于非遗项目、手工艺者、活动）
def get_number(request):
    print('get_number:::::::::::::::::???????????')
    if request.method == 'GET':
        print('!!!!!!!!!!!!!11!!!111111111111111111111111111')
    if request.method == "POST":
        # print('POST')
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
        # print(lis)
        # print('table:', table, 'num:', num)
        return JsonResponse({'num': num})

# 非遗代表作名录部分 MasterPieces ----------------------------
# 获取代表作名录的信息
def get_masterpieces(request):
    print('get_masterpieces')
    masterpieces_list = models.MasterPieces.objects.all()
    print(masterpieces_list)
    masterpieces = []
    for value in masterpieces_list:
        dic = {}
        dic = model_to_dict(value)
        dic['img_path'] = get_masterpieces_img(model_to_dict(value)['pieces_name_ch'])
        print('dic:', dic)
        masterpieces.append(dic)
    print('masterpieces:', masterpieces)
    return JsonResponse({'masterpieces':masterpieces})

# 获取代表作名录的图片路径，返回第一个横版图片
def get_masterpieces_img(name):
    directory_name = 'culapp/static/img/index/MasterPieces/' + name + '/项目/img/'       #文件夹路径
    for filename in os.listdir(directory_name):
        # print('filename:', filename)
        if if_horizon(directory_name + filename):
            # print('directory_name + filename',directory_name + filename)
            img_path = 'static/img/index/MasterPieces/' + name + '/项目/img/'+ filename
            return img_path


    # return masterpieces_img_path

# 判断图片是横版还是竖版
def if_horizon(src):
    img = Image.open(src)
    w,h = img.size
    if w >= h:
        return  True
    return  False

# 获取代表作名录的详情页url
def get_detailurl_masterpieces(request):
    if request.method == 'POST':
        name_ch = request.POST.get('name', False)
        work = models.MasterPieces.objects.filter(pieces_name_ch = name_ch)
        # name_en = {}
        print('work:', work)
        for value in work:
            name_en = model_to_dict(value)['pieces_name_en']
        print(name_en)
        name_en= ''.join(name_en.split())
        url = 'works_detail/' + name_en
        print('url:', url)
        return  JsonResponse({'url':url})


# 手工艺者部分 ------------------------------------

# 获取手工艺者的信息
def get_craftsman(request):
    # print('get_craftsman()')
    craftsman_list = models.Craftsman.objects.all()
    # print(craftsman_list)
    craftsman = []
    for value in craftsman_list:
        dic = {}
        # print('type', type(model_to_dict(value)))
        dic = model_to_dict(value)
        dic['item'] = get_pieces_name(model_to_dict(value)['item'])
        craftsman.append(dic)
        # print('dic:', dic)
        # get_pieces_name(model_to_dict(value)['item'])
    # print('craftsman:',craftsman)
    return JsonResponse({'craftsman':craftsman})

# 根据craftaman表中的item查询非遗项目名称
def get_pieces_name(item):
    pieces = models.MasterPieces.objects.filter(pieces_id = item)
    for value in pieces:
        pieces_name_en = model_to_dict(value)['pieces_name_ch']
    # print('name:', pieces_name)
    return pieces_name_en

# 根据任务名称，获取对应人物图像路径
def get_craftsman_img(request):
    if request.method == 'POST':
        name = request.POST.get('name', False)
        # print('name:', name)
        craftsman_img_path = 'img/index/Craftsman/' + name + '.png'
        # print('craftsman_img_path', craftsman_img_path)
        return JsonResponse({'craftsman_img_path':craftsman_img_path})

# 获取代表作名录的详情页url
def get_detailurl_craftsman(request):
    if request.method == 'POST':
        name_craftsman = request.POST.get('name', False)
        name_craftsman = name_craftsman.split('：')[-1]
        craftsman = models.Craftsman.objects.filter(craftsman_name_ch = name_craftsman)
        print('craftsman:', craftsman)
        for value in craftsman:
            name_en = model_to_dict(value)['craftsman_name_en']
        print(name_en)
        url = 'craftsman_detail/' + name_en
        return JsonResponse({'url': url})