from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain(request):
    return HttpResponse('<h1>Rohit Sharma is the captain of mi</h1>')
def vicecaptain(request):
    return HttpResponse('<h1>Hardik is the vicecaptain of mi</h1>')
