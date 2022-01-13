# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Teams, Players

def hello(request):
    return HttpResponse('''
    <h1>Hello Django!</h1>
    <ul>
        <li><a href="../teams/">Teams</a></li>
        <li><a href="../players/">Players</a></li>
    </ul>
    ''')


def teams(request):
    teams=Teams.objects.all()
    return HttpResponse(f'''
    <h1>This is the Teams page!</h1>
    <ul>
        <li>{teams[0].name}</li>
        <li>{teams[1].name}</li>
    </ul>
    ''')

def players(request):
    players=Players.objects.all()
    return HttpResponse(f'''
    <h1>This is the Players page!</h1>
    <ul>
        <li>{players[0].name}</li>
        <li>{players[1].name}</li>
    </ul>
    ''')