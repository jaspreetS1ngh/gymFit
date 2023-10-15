from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



# Create your views here.

def Home(request):
    return render(request,"index.html")

def SignUp(request):
    if request.method=='POST':
        username=request.POST.get('usernumber')
        email= request.POST.get('email')
        pass1= request.POST.get('pass1')
        pass2= request.POST.get('pass2')

        if len(username)>10 or len(username)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/SignUp')

        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/SignUp')
       
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/SignUp')
           
        except Exception as identifier:
            pass
        
        
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/SignUp')
           
        except Exception as identifier:
            pass

        myuser= User.objects.create_user(username,email,pass1)
        myuser.save
        messages.success(request,'User created')
        return redirect('/HandleLogin')

        
    return render(request,"signup.html")

def handleLogin(request):
    if request.method=='POST':
        username=request.POST.get('usernumber')
       
        pass1= request.POST.get('pass1')
        
        myuser= authenticate(username=username,password=pass1)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,'Logged in')
            return redirect('/')
        else:
            messages.error(request,'user not exits')
            return redirect('/HandleLogin')
            
        
    return render(request,"handleLogin.html")
