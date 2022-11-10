from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.

def main(request):
    if request.method == "GET":
        return HttpResponse('Hello')

def hello(request):
    if request.method == "GET":
        return HttpResponse('Hello! Its my project')

today = datetime.date.today()
def now_date(request):
    if request.method == 'GET':
        return HttpResponse(today)


def goodby(request):
    if request.method == "GET":
        return HttpResponse('Goodbye user!')