from django.shortcuts import render,redirect
from . models import *

def home(request):
    return render(request,'dashboard/homepage.html')

def course(request):
    return render(request,'dashboard/course.html')

def login(request):
        if request.method=='POST':
            email=request.POST['email']
            password=request.POST['password']
            try:
                 cust=Customer.objects.get(email=email,repass=password)
                 request.session['customer']=cust.id
                 return redirect('dashboard:newhomepage')
            except Customer.DoesNotExist:
                 return render(request,'dashboard/login.html',{'msg':'invalid username or password'})
        return render(request,'dashboard/login.html')

def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        password=request.POST['repass']
        cust=Customer(name=name,email=email,mob=number,repass=password)
        cust.save()
        return redirect("dashboard:login")

    return render(request,'dashboard/signup.html')

def newhomepage(request):
     course=Course.objects.all()
     return render(request,'dashboard/newhomepage.html',{'courses':course})

def logout(request):
     if 'customer' in request.session:
          del request.session['customer']
          return redirect('dashboard:home')
     



# Create your views here.
