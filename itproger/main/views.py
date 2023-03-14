from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h4>Проверка работы</h4>')

def about(request):
    return HttpResponse('<h4>Страница о нас</h4>')

def inspiration(request):
    return HttpResponse('<h3>Арсленго, ты станешь гуру в области разработки!</h3>')