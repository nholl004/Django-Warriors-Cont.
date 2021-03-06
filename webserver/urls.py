"""webserver URL Configuration

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
from server import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.test),
    # path('test1/',views.test1),
    # path('searching/', views.searching),
    # path('searched/', views.searched),
    path('', views.search),
    path('search',views.search),
    path('backup',views.backup),
    path('delete',views.delete),
    path('insert',views.insert),
    path('update',views.update),
    path('import',views.importButton),
    path('cases',views.top_cases),
    path('ConfirmtoDeath',views.confirm_to_death),
    path('rate',views.rec_Rate),
    path('peakdays', views.peakdays),
    path('daily',views.daily_cases),
    path('compare',views.compareTwo),
    path('dailydeaths',views.daily_deaths),
    path('casefatality', views.caseFatalityRatio),
    path('dailyrecov',views.daily_recov),
]
