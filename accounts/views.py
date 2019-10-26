
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Destination1

# Create your views here.
def regester(request):
    if request.method =='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password= request.POST['password']
        email = request.POST['email']

        if User.objects.filter(username=username).exists():
            messages.info(request,'Username is taken')
            return redirect("regester")
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email is taken')
            return redirect("regester")

        else:
            user= User.objects.create_user(username= username,password= password ,email= email,first_name=first_name, last_name=last_name)
            user.save();
            print("user created")
            return redirect('login')



    return render(request,'regester.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is  not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'Invalid User')
            return redirect('login')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")




def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')



def destinations(request):
    des = Destination1.objects.all()
    return render(request, "destinations.html", {'des': des})