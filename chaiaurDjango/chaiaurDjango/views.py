from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello, World! This is the Django Home Page.')
    return render(request, 'Home/index.html')

def about(request):
    return HttpResponse('This is the Django About Page.')

def contact(request):
    return HttpResponse('This is the Django Contact Page.')

def services(request):
    return HttpResponse('This is the Django Services Page.')

def blog(request):
    return HttpResponse('This is the Django Blog Page.')

def portfolio(request):
    return HttpResponse('This is the Django Portfolio Page.')

def pricing(request):
    return HttpResponse('This is the Django Pricing Page.')

def team(request):
    return HttpResponse('This is the Django Team Page.')

def faq(request):
    return HttpResponse('This is the Django FAQ Page.')

def terms(request):
    return HttpResponse('This is the Django Terms Page.')

def privacy(request):
    return HttpResponse('This is the Django Privacy Page.')





