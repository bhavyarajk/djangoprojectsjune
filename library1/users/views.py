from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.views import View

from users.forms import SignupForm

from users.forms import LoginForm


class Register(View):
    def post(self,request):
        form_instance = SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:home')
    def get(self,request):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request,'register.html',context)

from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
class UserLogin(View):
    def post(self,request):
        form_instance = LoginForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.cleaned_data['username']
            p=form_instance.cleaned_data['password']

            user=authenticate(username=u,password=p)
            if user:
                login(request,user)
                return redirect('books:home')
            else:
                messages.error(request,"invalid user credentials")
                return render(request,'login.html',{'form':form_instance})
    def get(self,request):
        form_instance=LoginForm()
        context={'form':form_instance}
        return render(request,'login.html',context)
class UserLogout(View):
    def get(self,request):
        logout(request)
        return redirect('users:login')





