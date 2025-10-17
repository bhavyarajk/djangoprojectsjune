from django.shortcuts import render,redirect
from app1.models import Moviedetail
def home(request):
    if(request.method=="GET"):
        m=Moviedetail.objects.all()
        context={'movies':m}
        return render(request,'home.html',context)
from app1.forms import MovieForm
def add(request):
    if(request.method=="POST"): #after submission
        form_instance=MovieForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return render(request,'addmovie.html')


    if (request.method == "GET"):
        form_instance=MovieForm()
        context={'form':form_instance}
        return render(request, 'addmovie.html',context)