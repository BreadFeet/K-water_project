from django.shortcuts import render
from django.http import HttpResponse
import json
from myanalysis.analysis import waterAnal, healthAnal


# Create your views here.
def main(request):
    return render(request, 'main.html')

def chart1_1(request):
    return render(request, 'chart1_1.html')

def chart1_2(request):
    return render(request, 'chart1_2.html')

def chart1_3(request):
    return render(request, 'chart1_3.html')

def chart2_1(request):
    return render(request, 'chart2_1.html')

def chart2_2(request):
    return render(request, 'chart2_2.html')

def chart3(request):
    return render(request, 'chart3.html')

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