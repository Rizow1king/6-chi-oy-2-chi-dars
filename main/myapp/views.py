from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def home(request: WSGIRequest):
    return render(request, 'home.html')


def calculator(request: WSGIRequest):
    return render(request, 'calculator.html')


def timer(request: WSGIRequest):
    return render(request, 'timer.html')


def convertor(request: WSGIRequest):
    return render(request, 'converter.html')


def game(request: WSGIRequest):
    return render(request, 'game.html')


def randomiser(request: WSGIRequest):
    return render(request, 'randomiser.html')


def notepad(request: WSGIRequest):
    return render(request, 'notepad.html')


def shtrih(request: WSGIRequest):
    return render(request, 'shtrih.html')


def metres(request: WSGIRequest):
    return render(request, 'metres.html')


def payment(request: WSGIRequest):
    return render(request, 'payment.html')


def table(request: WSGIRequest):
    return render(request, 'table.html')
