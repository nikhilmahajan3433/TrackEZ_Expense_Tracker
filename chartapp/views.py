from tkinter import Entry
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render

from chartapp.models import exp_add
from mysite.models import transac,income

def chart(request):
    # labels=['A','B','C','D','E']
    # data=[11,32,98,55,6]
    # out={'labels':labels,'data':data}
    # return render(request,'chart.html',out)
    data=transac.objects.all()
    inc=income.objects.all()
    expense5=transac.objects.filter().order_by('-val')[:5][::-1]
    income5=income.objects.filter().order_by('-value')[:5][::-1]
    return render(request,'chart.html',{'data':data,'exp5':expense5,'inc5':income5,'inc':inc})

def data_exp(request):
    return render(request,'exp.html')

def data_add(request):
    if request.method=="GET":
        if request.GET.get("field") and request.GET.get("values"):
            add=exp_add()
            add.name=request.GET.get("field")
            add.value=request.GET.get("values")
            add.save()
            return HttpResponse("Added")
        else:
            return HttpResponse("Not added")

def data_show(request):
    field=Entry.objects.all('name')
    data=Entry.objects.all('value')
    

def trans(request):
    trans=exp_add.objects.all()
    return render(request,'transaction.html',{'trans':trans})
