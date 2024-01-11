from django.shortcuts import redirect, render
from django.http import HttpResponse
#from appname.models import task
from todoapp.models import Task
def display(request):
    # obj={
    #     'task':[
    #         {'name':"Drinking Water",'time':'6:00 AM'},
    #         {'name':"Exercise",'time':'6:30 AM'},
    #         {'name':"Breakfast ",'time':'7:00 AM'},
    #     ]
    # }
    dt=Task.objects.all()
    obj1={'task':dt}
    return render(request,'task.html',obj1)

def add(request): 
    if request.method=='GET':
    
        return render(request,'add.html')
    else:
        # print(request.method)
        # name of task
        nm=request.POST['name']
        t=request.POST['time']
        obj=Task.objects.create(name=nm,time=t)
        obj.save()
        # return HttpResponse('form submitted'+nm+ t)
        return redirect('/')
    #edit------------------------------------------------------------ - 
def edit(request,tid):
    if request.method=='GET':
        obj=Task.objects.filter(id=tid)
        return render(request,'edit.html',{'task':obj})
    else:
        nm=request.POST['name']
        t=request.POST['time']
        obj=Task.objects.filter(id=tid)
        obj.update(name=nm,time=t)
    return redirect('/')
    

#DELETE---------------------------------------------------------------------------------
def delete(request,tid):
    obj=Task.objects.filter(id=tid)
    obj.delete()
    return redirect('/')

