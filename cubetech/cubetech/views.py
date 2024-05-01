from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request,"index.html")

def aboutUs(request):
    return HttpResponse("Welcome to Cubetech..")

def Course(request):
    return HttpResponse("Welcome to Cubetech111..")

def courseDetails(request,courseid):
    return HttpResponse(courseid)