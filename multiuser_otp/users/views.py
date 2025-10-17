from django.shortcuts import render,redirect


from django.views import View
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class AdminHome(View):
    def get(self,request):
        return render(request,'adminhome.html')
class StudentHome(View):
    def get(self,request):
        return render(request,'studenthome.html')
class TeacherHome(View):
    def get(self,request):
        return render(request,'teacherhome.html')
from users.forms import SignupForm
from django.core.mail import send_mail
class Register(View):
    def post(self, request):
        form_instance = SignupForm(request.POST)
        if form_instance.is_valid():
            u=form_instance.save(commit=False)
            u.is_active=False
            u.save()
            u.generate_otp()
            send_mail(
                "Django Auth OTP",
                u.otp,
                "bhavyaluminar@gmail.com",
                [u.email],
                fail_silently=False,
            )

            return redirect('verify')
        else:
            print('error')
            return render(request, 'register.html', {'form': form_instance})

    def get(self, request):
        form_instance = SignupForm()
        context = {'form': form_instance}
        return render(request, 'register.html', context)
from django.contrib.auth import authenticate,login,logout
from users.forms import LoginForm
from django.contrib import messages
class UserLogin(View):

        def post(self, request):
            form_instance = LoginForm(request.POST)
            if form_instance.is_valid():
                u = form_instance.cleaned_data['username']
                p = form_instance.cleaned_data['password']
                user = authenticate(username=u, password=p)
                # authenticate() returns user object if user with the given username and password exist
                # else returns none
                if user and user.is_superuser==True:  # if admin user
                    login(request, user)  # login() adds the current user into session
                    return redirect('adminhome')
                elif user and user.role=='student': #if student user
                    login(request, user)  # login() adds the current user into session
                    return redirect('studenthome')
                elif user and user.role == 'teacher':#if teacher user
                    login(request, user)  # login() adds the current user into session
                    return redirect('teacherhome')

                else:
                    messages.error(request, 'invalid user credentials')
                    return render(request, 'login.html', {'form': form_instance})

        def get(self, request):
            form_instance = LoginForm()
            context = {'form': form_instance}
            return render(request, 'login.html', context)
class UserLogout(View):
    def get(self,request):
        return render(request,'home.html')


from users.models import CustomUser
class Otp_verify(View):
    def post(self,request):
        o=request.POST['o']
        try:
            u=CustomUser.objects.get(otp=o)  #if user record with matching otp exists
            u.is_verified=True
            u.is_active=True
            u.otp=None
            u.save()
            return redirect('login')
        except:  #if user does not exist
            messages.error(request,'Invalid otp')
            return redirect('verify')
    def get(self,request):
        return render(request,'verify.html')