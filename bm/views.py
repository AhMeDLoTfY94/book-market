from django.shortcuts import render
from .models import *
from .forms import BookForm ,CategoryForm

def index(request):
          if request.method == "POST":
                    data=BookForm(request.POST,request.FILES)
                    if data.is_valid():   
                              data.save()
                    add_category=CategoryForm(request.POST)
                    if add_category.is_valid():
                              add_category.save()
                              
          books    =Book.objects.all()
          categorys=Category.objects.all()
          form     = BookForm()
          formc    = CategoryForm()
          context={
                    'books':books,
                    'categorys':categorys,
                    'form'     :form,
                    'formc'    :formc,
                    
          }
          return render(request,'pages/index.html',context)


def books(request):
          if request.method == "POST":
                    
                    add_category=CategoryForm(request.POST)
                    if add_category.is_valid():
                              add_category.save()
                              
          books    =Book.objects.all()
          categorys=Category.objects.all()
          formc    = CategoryForm()
          context={
                    'books'    :books,
                    'categorys':categorys,
                    'formc'    :formc,
                    
                    
          }
          return render(request,'pages/books.html',context)