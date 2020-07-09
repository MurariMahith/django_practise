from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def xyz(request):
    return render(request,'home.html',{'name':'mahith'})

def test(request):

    return HttpResponse("<h1> hello testing working</h1>")

def test2(request):
    return HttpResponse("<h1>test2 from double mappingworking")

def product(request):

    return HttpResponse("<h1>products</h1>")

def add(request):

    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1+val2

    return render(request, 'result.html', {'result':res});