# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def test(request):
    return HttpResponse('''
    <h1>This is a test page!</h1>
    <a href="../hello/"/>
    <img src='https://assets-fr.imgfoot.com/media/cache/642x382/lionel-messi-2122-psg-61a5316611f51.jpg'>
    </a>
    ''')