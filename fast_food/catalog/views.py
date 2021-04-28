from django.shortcuts import render
from .models import Product_image

def catalog(request):
    context={

    }
    return render(request, 'index.html',context)
