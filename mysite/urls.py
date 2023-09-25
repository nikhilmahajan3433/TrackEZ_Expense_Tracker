"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from . import views
from chartapp.views import data_exp,trans

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.style_login,name='home'),
    # path('log',views.index,name='index'),
    path('out',views.vals,name='vals'),
    path('about/',views.about,name='about'),
    path('upload/',views.usr_upload,name='upload'),
    path('display/',views.display_data,name='display_data'),
    path('log/',views.log,name='log'),
    path('log/login',views.log_in,name='log_in'),
    # path('login',views.log_in,name="login"),  #ithe change kelay
    path('home/',views.home,name='signup'),
    path('home/upload',views.usr_upload,name='upload'),
    path('cht/',include('chartapp.urls')),
    path('exp/data_exp',data_exp,name='data_exp'),
    path('exp/data_add',views.data_add,name='data_add'),
    path('trans/',trans,name='trans'),
    path('dets',views.trans_data,name='dets'),
    path('exp/',views.exp,name="exp"),
    path('style_login/',views.style_login,name='style_login'),
    path('style_login/login',views.log_in,name=" style_login/login"),
    path('style_login/style_login/upload',views.usr_upload,name='style_login/upload'),
    # path('side',views.side,name='side'),
    # path('side',include('dashboard.urls')),
    path('login',include('dashboard.urls')),
    path('data_add',views.data_add,name="data_add"),
    path('income_data',views.income_data,name="income_data"),
    path('export_excel',views.export_excel,name="export_excel"),
    # path('homepage/',views.homep,name='homep'),
    
]
