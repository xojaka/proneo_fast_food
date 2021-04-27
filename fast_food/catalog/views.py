from django.shortcuts import render

def catalog(request):
    return render(request, 'index.html',{})
