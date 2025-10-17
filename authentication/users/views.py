from django.shortcuts import render,redirect
from django.views import View
class Home(View):
    def get(self,request):
        return render(request,'home.html')
from users.forms import SignupForm,LoginForm
from django.contrib.auth.forms import UserCreationForm
class Register(View):
    def post(self,request):
        form_instance=SignupForm(request.POST)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('login')
        else:
            print('error')
            return render(request,'register.html',{'form':form_instance})
    def get(self,request):
        form_instance=SignupForm()
        context={'form':form_instance}
        return render(request,'register.html',context)
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

class Userlogout(View):
     def get(self,request):
         logout(request)
         return redirect('login')




