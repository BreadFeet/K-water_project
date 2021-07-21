from django.shortcuts import render
from django.http import HttpResponse
import json
from myanalysis.analysis import waterAnal, healthAnal


# Create your views here.
def main(request):
    return render(request, 'main.html')

def chart1(request):
    return render(request, 'chart1.html')

def chart2(request):
    return render(request, 'chart2.html')

def chart3(request):
    return render(request, 'chart3.html')

def ml(request):
    return render(request, 'ml.html')


def chart1s(request):
    loc = request.GET['loc']
    result = waterAnal.locWaterQual(loc)
    return HttpResponse(json.dumps(result), content_type='application/json')

def chars2s(request):
    loc = request.GET['loc']
    result = healthAnal.locHealthQual(loc)
    return HttpResponse(json.dumps(result), content_type='application/json')