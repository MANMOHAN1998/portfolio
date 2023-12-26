from django.shortcuts import render, HttpResponse

# Create your views here.


def first_function(request):
    return render(request,'index.html')

def intro(request):
    return render(request,'intro.html')

def blogs(request):
    return render(request,'blog.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')