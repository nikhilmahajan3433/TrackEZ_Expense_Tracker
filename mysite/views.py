from datetime import datetime,date
from email import message
from pickle import TRUE
from urllib import response
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import context,Template
from django.contrib import messages
from .models import income, transac, usrs
import xlwt

def home(request):
    return render(request,'signup.html')
def index(request):
    # usname=request.GET['username']
    # pasw=request.GET['pass']
    # print(usname,pasw)
    # return render(request,'output.html',{'username':usname,'password':pasw})
    return HttpResponse("Index")
def vals(request):
    if request.method=="POST":
        usname=request.POST.get('username')
        psw=request.POST.get('pass')
        # context=context({'username':usname,'pass':psw})
        # return render(request,'output.html',context)
    params={'username':usname,'password':psw}
    return render(request,'output.html',params)
    # print(usname,psw)

def usr_upload(request):
    if request.method=='GET':
        if request.GET.get('username') and request.GET.get('pass'):
            upl=usrs()
            upl.name=request.GET.get('username')
            upl.passw=request.GET.get('pass')
            upl.save()

            return HttpResponse('Succesful')
    else:
        return HttpResponse('Unsuccesful')

def display_data(request):
    all_data=usrs.objects.all()
    info={'data':all_data}
    # for object in all_data:
    #     print(object.name)
    return render(request,'out_data.html',info)

def log(request):
    return render(request,'login.html')
def log_in(request):
    nm=request.GET.get('uname')
    p=request.GET.get('pss')
    login_data=usrs.objects.all()
    for object in login_data:
        if(nm==object.name and p==object.passw):
            # return HttpResponse("User found")
            # return render(request,'index.html')
            return render(request,'dashboard/sidebar.html')
            break
    else:
        return HttpResponse("User not found")  
def about(request):
    return HttpResponse("About Django")

def homep(request):
    return render(request,'homepage.html')

def exp(request):
    return render(request,'index.html')

def style_login(request):
    return render(request,'login_index.html')

def data_add(request):
    if request.method=="GET":
        if request.GET.get('trans') and request.GET.get('value'):
                trns=transac()
                trns.trans=request.GET.get('trans')
                trns.val=request.GET.get('value')
                if request.GET.get('date'):
                    trns.dtime=request.GET.get('date')
                else:
                    trns.dtime=date.today()
                trns.save()
                return redirect('side')
                # return HttpResponse("Added")
                messages.success(request,'Data Added')
        else:
            # return HttpResponse("Not Added")
            messages.success(request,'Not Added')
            return redirect('side')
        #         return render(request,'dashboard/sidebar.html')
        # else:
        #     return render(request,'dashboard/sidebar.html')

def income_data(request):
    if request.method=='GET':
        if request.GET.get('inc') and request.GET.get('inc_val'):
            inc=income()
            inc.title=request.GET.get('inc')
            inc.value=request.GET.get('inc_val')
            if request.GET.get('inc_date'):
                inc.timestamp=request.GET.get('inc_date')
            else:
                inc.timestamp=date.today()
            inc.save()
            return redirect('side')
def trans_data(request):
    trans_details=transac.objects.all()
    return render(request,'transac.html',{'dets':trans_details})

# def side(request):
#     return render(request,'sidebar.html')

def export_excel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition']='attachment; filename=Expenses' + \
        str(date.today())+ '.xls'
    date1=request.GET.get('d1')
    date2=request.GET.get('d2')
    
    data1=transac.objects.filter(dtime__lte=date2, dtime__gte=date1).values_list('val','trans','dtime')

    # data1=transac.objects.values_list('val','trans','dtime')
    
    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Expenses')
    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=TRUE
    columns=['Amount','Description','Date']
    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num],font_style)

    # data1=[(1,2,3),(4,5,6),(7,8,9)]
    for row in data1:
        row_num+=1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]))
    wb.save(response)
    print(data1)
    return response
    