from django.shortcuts import render
from django.http import HttpResponse
import json
from myanalysis.analysis import waterAnal, healthAnal


# Create your views here.
def main(request):
    return render(request, 'main.html')

def info1(request):
    return render(request, 'info11.html')

def chart1_1(request):
    return render(request, 'chart1_1.html')

def chart1_2(request):
    return render(request, 'chart1_2.html')

def chart1_3(request):
    return render(request, 'chart1_3.html')


def info2(request):
    return render(request, 'info22.html')

def chart2_1(request):
    return render(request, 'chart2_1.html')

def chart2_2(request):
    return render(request, 'chart2_2.html')


def info3(request):
    return render(request, 'info33.html')

def ml1(request):
    return render(request, 'ml1.html')

def ml2(request):
    return render(request, 'ml2.html')


def reflection(request):
    return render(request, 'reflection.html')

def ml(request):
    return render(request, 'ml.html')


def chart1s(request):
    loc = request.GET['loc']
    result = waterAnal.locWaterQual(loc)
    return HttpResponse(json.dumps(result), content_type='application/json')

def chart2s(request):
    fx = request.GET['fx']
    if fx == '1':
        loc = request.GET['param']
        result = healthAnal.locHealthQual(loc)
    elif fx == '2':
        year = int(request.GET['param'])         # 문자열 -> int
        result = healthAnal.healthMap(year)
    return HttpResponse(json.dumps(result), content_type='application/json')