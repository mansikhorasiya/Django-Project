from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
        # data={
        #      'title':'Home new',
        #      'bdata':'Welcome to cubetech || Jodhpur',
        #      'clist':['python' , 'java' , 'php'],
        #      'number':[10,20,30,40,50],
        #      'StudentDetails':[
        #           {'name':'Testing1','phone':9876547895},
        #           {'name':'Testing2','phone':9888765478}
        #      ]
        # }

        return render(request,"index.html")

def about(request):
    return render(request,"index.html")

def generic(request):
      return render(request,"generic.html")

def element(request):
     
     return render(request,"elements.html")

def Course(request):
    return HttpResponse("Welcome to Cubetech111..")

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def userform(request):
    finaleans=0
    try:
        # n1=int(request.GET['num1'])
        # n2=int(request.GET['num2'])
        n1=int(request.GET.get('num1'))
        n2=int(request.GET.get('num2'))
        # print(n1+n2)
        finaleans=n1+n2

    except:
      pass

    return render(request,"userform.html",{'output':finaleans})
