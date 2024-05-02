from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
        data={
             'title':'Home new',
             'bdata':'Welcome to cubetech || Jodhpur',
             'clist':['python' , 'java' , 'php'],
             'StudentDetails':[
                  {'name':'Testing1','phone':9876547895},
                  {'name':'Testing2','phone':9888765478}
             ]
        }

        return render(request,"index.html",data)

def aboutUs(request):
    return HttpResponse("Welcome to Cubetech..")

def Course(request):
    return HttpResponse("Welcome to Cubetech111..")

def courseDetails(request,courseid):
    return HttpResponse(courseid)