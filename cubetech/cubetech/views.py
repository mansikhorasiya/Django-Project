from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import UsersForm
from service.models import service
from news.models import News

def homePage(request):
        newsData=News.objects.all();
        servicesData =service.objects.all().order_by('service_title')[:6]
     #    for a in servicesData:
     #         print(a.service_title)
     #    print(service)
        data={
             'servicesData':servicesData,
             'newsData':newsData
        }
        return render(request,"index.html",data)

def newsDetails(request,newsid):
    newsDetails=News.objects.get(id=newsid)
    print(newsid)
    data={
         'newsDetails':newsDetails
    }
    return render(request,"newsDetails.html",data)

def about(request):
    return render(request,"index.html")

def generic(request):
      return render(request,"generic.html")

def element(request):
     return render(request,"elements.html")

def saveevenood(request):
     c=''
     if request.method=='POST':
          if request.POST.get('num1')=='':
               return render(request,"evenodd.html",{'error':True})

          n=int(request.POST.get('num1'))
          if n%2==0:
               c='Even Number'
          else:
               c='Odd Number'

     return render(request,"evenodd.html",{'c':c})

def marksheet(request):
    if request.method=="POST":
        s1=int(request.POST.get('subject1'))
        s2=int(request.POST.get('subject2'))
        s3=int(request.POST.get('subject3'))
        s4=int(request.POST.get('subject4'))
        s5=int(request.POST.get('subject5'))
        t=s1+s2+s3+s4+s5
        p=t*100/500;
        if p>=60:
             d='First div'
        elif p>=48:
             d='Second div'
        elif p>=35:
             d='Third div'
        else:
             d='fail'
        data={
             'totle':t,
             'persantages':p,
             'divsion':d
        } 
        print(t) 
        return render(request,"marksheet.html",data)
    return render(request,"marksheet.html")


def calculator(request):
     c=''
     try:
          if request.method=="POST":
               n1=eval(request.POST.get("num1"))
               n2=eval(request.POST.get("num2"))
               opr=request.POST.get("opr")
               if opr=='+':
                    c=n1+n2;
               elif opr=='-':
                    c=n1-n2
               elif opr=='*':
                    c=n1*n2
               elif opr=='/':
                    c=n1/n2
     except :
        print(c)
     return render(request,"calculator.html",{'c':c})


def Course(request):
    return HttpResponse("Welcome to Cubetech111..")

def courseDetails(request,courseid):
    return HttpResponse(courseid)

def submitform(request):
      return HttpResponse(request)

def userform(request):
    finaleans=0
    fn=UsersForm
    data={'form':fn}
    try:
        if request.method=="POST":
        # n1=int(request.GET['num1'])
        # n2=int(request.GET['num2'])
            n1=int(request.GET.get('num1'))
            n2=int(request.GET.get('num2'))
            # print(n1+n2)
            finaleans=n1+n2
            data={
                 'form':fn,
                #  'n1':n1,
                #  'n2':n2,
                 'output':finaleans

            }

            return HttpResponseRedirect('/about/')

    except:
      pass

    return render(request,"userform.html",{'output':finaleans})
    



