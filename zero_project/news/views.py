from django.shortcuts import render
from django.http import HttpResponse

from .models import Arts

def index(request):   #request экземпляр класса HttpRequest собраны данные из запроса
    news = Arts.objects.all()

    return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})

def test(request):
    return HttpResponse('<h1> Test page</h1>')