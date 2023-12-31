from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from authentication.models import Contact,MembershipPlan,Trainer,Enrollment,Gallery,Attendance



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

def handlelogout(request):
    logout(request)
    messages.success(request,"user loged out")
    return redirect('/HandleLogin')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('fullname')
        email=request.POST.get('email')
        number=request.POST.get('num')
        desc=request.POST.get('desc')
        myquery=Contact(name=name,email=email,phonenumber=number,description=desc)
        myquery.save()       
        messages.info(request,"Thanks for Contacting us we will get back you soon")
        return redirect('/contact')
        
    return render(request,"contact.html")

def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/HandleLogin')
    
    membership=MembershipPlan.objects.all()
    trainer=Trainer.objects.all()
    context={"Membership":membership,"Trainer":trainer}
    if request.method=="POST":
        FullName=request.POST.get('FullName')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        PhoneNumber=request.POST.get('PhoneNumber')
        DOB=request.POST.get('DOB')
        member=request.POST.get('member')
        trainer=request.POST.get('trainer')
        reference=request.POST.get('reference')
        address=request.POST.get('address')
        query=Enrollment(FullName=FullName,Email=email,Gender=gender,PhoneNumber=PhoneNumber,DOB=DOB,SelectMembershipplan=member,SelectTrainer=trainer,Reference=reference,Address=address)
        query.save()
        messages.success(request,"Thanks For Enrollment")
        return redirect('/join')

    return render(request,"enroll.html",context)

def viewprofile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/HandleLogin')
    number=request.user
    posts=Enrollment.objects.filter(PhoneNumber=number)
    attendance=Attendance.objects.filter(phonenumber=number)
    context={"posts":posts,"attendance":attendance}

    return render(request,"profile.html",context)


def gallery(request):
    posts= Gallery.objects.all()
    context={"posts":posts}
    return render(request,"gallery.html",context)
def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    SelectTrainer=Trainer.objects.all()
    context={"SelectTrainer":SelectTrainer}
    if request.method=="POST":
        phonenumber=request.POST.get('PhoneNumber')
        Login=request.POST.get('logintime')
        Logout=request.POST.get('loginout')
        SelectWorkout=request.POST.get('workout')
        TrainedBy=request.POST.get('trainer')
        query=Attendance(phonenumber=phonenumber,Login=Login,Logout=Logout,SelectWorkout=SelectWorkout,TrainedBy=TrainedBy)
        query.save()
        messages.warning(request,"Attendace Applied Success")
        return redirect('/attendance')
    return render(request,"attendance.html",context)