from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,"index.html")

def SignUp(request):
    return render(request,"signup.html")
def handleLogin(request):
    return render(request,"handleLogin.html")
