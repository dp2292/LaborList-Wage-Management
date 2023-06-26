from django.shortcuts import render,redirect
from labor_register import models
from labor_register import forms
from django.contrib import messages
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.db import connection

# Create your views here.
def default_page(request):
    return render(request,'index.html')


# labor CRUD operation + sort
def showlabor(request):
    labor_data = models.Labor.objects.all()
    return render(request, 'labor_list.html',{'data' :labor_data})

def sorted_labor(request):
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            labor_data = models.Labor.objects.all().order_by(type)
            messages.success(request,'Sorted by '+type+' succesfully !')
            return render(request, 'labor_list.html',{'data':labor_data })
    else:
        return render(request, 'labor_list.html')   

def insert_labor(request,id=0):
    if request.method=='GET':
        if id==0:
            form = forms.LaborForm()
        else:
            labor = models.Labor.objects.get(pk=id)
            form =   forms.LaborForm(instance=labor) 
        return render(request, 'labor_form.html',{'form' :form})     
    else:
        if id==0:
            form = forms.LaborForm(request.POST)
            messages.success(request,'Inserted succesfully !') 
        else :
            labor = models.Labor.objects.get(pk=id)
            form =   forms.LaborForm(request.POST,instance=labor) 
            messages.success(request,'Updated succesfully !')    
        if form.is_valid():
            form.save()
        else:
            messages.error(request,'Form data is invalid.') 
        return redirect(showlabor)    

def delete_labor(request,id):
    labor = models.Labor.objects.get(pk=id)
    labor.delete()  
    messages.success(request,'Deleted succesfully !') 
    return redirect(showlabor)   



# Supervisor CRUD operation + sort

def showSupervisor(request):
    supervisor_data = models.Supervisor.objects.all()
    return render(request, 'supervisor_list.html',{'data' :supervisor_data})

def sortedsupervisor(request):  
    if request.method=="POST":
        if request.POST.get('Sort'):
            type=request.POST.get('Sort')
            supervisor_data = models.Supervisor.objects.all().order_by(type)
            messages.success(request,'Sorted by '+type+' succesfully !')
            return render(request, 'supervisor_list.html',{'data':supervisor_data })
    else:
        return render(request, 'supervisor_list.html')    

def insert_supervisor(request,id=0):
    if request.method=='GET':
        if id==0:
            form = forms.SupervisorForm()
        else:
        # read in from form    
            supervisor = models.Supervisor.objects.get(pk=id)
            form =   forms.SupervisorForm(instance=supervisor) 
        return render(request, 'supervisor_form.html',{'form' :form})     
    else:
        # simple create with post 
        if id==0:
            form = forms.SupervisorForm(request.POST)
            messages.success(request,'Inserted succesfully !') 
        # update option     
        else :
            supervisor = models.Supervisor.objects.get(pk=id)
            form =   forms.SupervisorForm(request.POST,instance=supervisor) 
            messages.success(request,'Updated succesfully !')    
        if form.is_valid():
            form.save()
        return redirect(showSupervisor)   

# delete operation
def delete_supervisor(request,id):
    supervisor = models.Supervisor.objects.get(pk=id)
    supervisor.delete()  
    messages.success(request,'Deleted succesfully !')
    return redirect(showSupervisor) 


def raw_query(request):
    cursor = connection.cursor()
    try:
        cursor.execute(request.POST.get('Query'))
    except:
        return HttpResponse("Query isn't right")    
    query_data=cursor.fetchall()
    dic = cursor.description
    new = dict()
    k = 0 
    for i in dic:
            new[i[0]] = i[0]
            k+=1             
    return render(request, 'query_result.html',{'data' :query_data , 'dic':new})

def query_show(request):
    return render(request,'query_run.html')

    

                

        

