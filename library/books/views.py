from django.shortcuts import render,redirect

from books.forms import BookForm


def home(request):
    if(request.method=="GET"):
        return render(request,'home.html')

# class classname(View):
#     def get(self,request):
#         #code
#     def post(self,request):
#         #code





from books.models import Book
def addbooks(request):
   if(request.method=="POST"): #after submission
       print(request.POST)
       print(request.FILES)
       form_instance=BookForm(request.POST,request.FILES)
       if(form_instance.is_valid()):
           form_instance.save()

           # data=form_instance.cleaned_data
           # print(data)
           # t=data['title']
           # a=data['author']
           # p=data['price']
           # pg=data['pages']
           # l=data['language']
           # b=Book.objects.create(title=t,author=a,price=p,pages=pg,language=l)
           # b.save()
           return redirect('books:viewbooks')

   if(request.method=="GET"): #Read Request
        form_instance=BookForm()
        context={'form':form_instance}
        return render(request, 'addbooks.html',context)

def viewbooks(request):
    b=Book.objects.all()  #to read all records from table
    context={'books':b}
    return render(request, 'viewbooks.html',context)

def bookdetail(request,i):
    if(request.method=="GET"):

        b=Book.objects.get(id=i)
        context={'book':b}
        return render(request,'bookdetail.html',context)
def editbook(request,i):


    if (request.method == "POST"):  # after submission
        b=Book.objects.get(id=i)
        form_instance = BookForm(request.POST, request.FILES,instance=b)
        if (form_instance.is_valid()):
            form_instance.save()
            return redirect('books:viewbooks')



    if (request.method == "GET"):
        b=Book.objects.get(id=i)
        form_instance=BookForm(instance=b)
        context={'form':form_instance}
        return render(request,'editbook.html',context)
def deletebook(request,i):

    b=Book.objects.get(id=i)
    b.delete()
    return redirect('books:viewbooks')

