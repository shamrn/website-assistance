from django.shortcuts import render
from .models import Category,Subcategory

def service(request):
    category = Category.objects.all()
    return render(request,'service/service.html',{'category':category})