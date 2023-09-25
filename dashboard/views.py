from django.shortcuts import render
from numpy import sinc
from pandas import date_range

from mysite.models import transac

def side(request):
    last=transac.objects.filter().last()
    line=transac.objects.all()
    top_five=transac.objects.filter().order_by('-dtime')[:5][::-1]
    data={'last_data':last,'line':line,'five':top_five}
    return render(request,'dashboard/sidebar.html',data)

def table(request):
    # data=transac.objects.all()
    data=transac.objects.filter().order_by('dtime').reverse()
    return render(request,'dashboard/table.html',{'data':data})


