from django.shortcuts import render,redirect
from .models import *
from .form import *
# Create your views here.

def index(request):
    if request.method == 'POST':
        add_book=Bookform(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()
            return redirect('/')
            
        add_cat=Categoryform(request.POST)
        if add_cat.is_valid():
            add_cat.save()
            return redirect('/')



    context={
        'books':Book.objects.all(),
        'category':category.objects.all(),
        'form': Bookform(),
        'catform':Categoryform(),
        'booksolid':Book.objects.filter(status='sold').count(),
        'bookrental':Book.objects.filter(status='rental').count(),
        'bookavailable':Book.objects.filter(status='available').count(),
    }
    return render(request,'pages/index.html',context=context)



def index2(request,id):
    if request.method == 'POST':
        add_book=Bookform(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()
            return redirect('/')
            
        add_cat=Categoryform(request.POST)
        if add_cat.is_valid():
            add_cat.save()
            return redirect('/')



    context={
        'books':Book.objects.filter(category_book=id),
        'category':category.objects.all(),
        'form': Bookform(),
        'catform':Categoryform(),
        'booksolid':Book.objects.filter(status='sold').count(),
        'bookrental':Book.objects.filter(status='rental').count(),
        'bookavailable':Book.objects.filter(status='available').count(),
    }
    return render(request,'pages/index.html',context=context)


def books(request):
    all_book=Book.objects.all()
    title=None
    if 'search_name' in request.GET:
        title=request.GET['search_name']
        if title:
            all_book=all_book.filter(title__icontains=title)

    context={
        'books':all_book,
        'category':category.objects.all(),
    }
    return render(request,'pages/books.html',context=context)


def updates(request,id):
    book=Book.objects.get(id=id)
    if request.method=='POST':
        bookform=Bookform(request.POST,request.FILES,instance=book)
        if bookform.is_valid():
            bookform.save()
            return redirect('/')
    else:
        bookform=Bookform(instance=book)

    context={
        'form':bookform,
    }

    return render(request,'pages/update.html',context)


def delete(request,id):
    book=Book.objects.get(id=id)
    if request.method=='POST':
         book.delete()
         return redirect('/')
    return render(request,'pages/delete.html')