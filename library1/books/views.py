from django.shortcuts import render,redirect

from books.forms import BookForm

#
# def home(request):
#
#     return render(request,'home.html')

from django.views import View
class Home(View):
    def get(self,request):
        return render(request,'home.html')



from books.models import Book
# def addbooks(request):
#    if(request.method=="POST"): #after submission
#        print(request.POST)
#        print(request.FILES)
#        form_instance=BookForm(request.POST,request.FILES)
#        if(form_instance.is_valid()):
#            form_instance.save()
#
#            # data=form_instance.cleaned_data
#            # print(data)
#            # t=data['title']
#            # a=data['author']
#            # p=data['price']
#            # pg=data['pages']
#            # l=data['language']
#            # b=Book.objects.create(title=t,author=a,price=p,pages=pg,language=l)
#            # b.save()
#            return redirect('books:viewbooks')
#
#    if(request.method=="GET"): #Read Request
#         form_instance=BookForm()
#         context={'form':form_instance}
#         return render(request, 'addbooks.html',context)

class Addbooks(View):
   def post(self,request): #after submission
       print(request.POST)
       print(request.FILES)
       form_instance=BookForm(request.POST,request.FILES)
       if(form_instance.is_valid()):
           form_instance.save()
           return redirect('books:viewbooks')

   def get(self,request): #Read Request
        form_instance=BookForm()
        context={'form':form_instance}
        return render(request, 'addbooks.html',context)
from django.db.models import Q
class SearchView(View):
    def get(self,request):
        query=request.GET['q']
        # print(query)

        if query:
            b=Book.objects.filter(Q(author__icontains=query)|Q(title__icontains=query)|Q(language__icontains=query))
            #Q object --syntax used to add logical or/logical and in ORM queries
            #field lookups -->fieldname__lookup eg:age__gt=30 /age__lt=30/title__contains="abc"/title__icontains="abc"
            context={'book':b}


            return render(request,'search.html',context)


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
