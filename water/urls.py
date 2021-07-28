"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from water import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),

    # path('info11', TemplateView.as_view(template_name='info11.html'), name='info11'),

    path('info1', views.info1, name='info1'),
    path('chart1_1', views.chart1_1, name='chart1_1'),
    path('chart1s', views.chart1s, name='chart1s'),
    path('chart1_2', views.chart1_2, name='chart1_2'),
    path('chart1_3', views.chart1_3, name='chart1_3'),

    path('info2', views.info2, name='info2'),
    path('chart2_1', views.chart2_1, name='chart2_1'),
    path('chart2s', views.chart2s, name='chart2s'),
    path('chart2_2', views.chart2_2, name='chart2_2'),

    path('info3', views.info3, name='info3'),
    path('ml1', views.ml1, name='ml1'),
    path('ml2', views.ml2, name='ml2'),
    path('reflection', views.reflection, name='reflection'),

    #path('chart3s', views.chart3s, name='chart3s'),
]
