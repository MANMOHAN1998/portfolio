from django.shortcuts import render, HttpResponse

# Create your views here.


def first_function(request):
    return render(request,'index.html')