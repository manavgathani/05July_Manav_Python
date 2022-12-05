from django.shortcuts import render
from .models import usersignup
from .forms import userSignupForm,notesform

# Create your views here.
def index(request):
    if request.method=='POST':
        if request.POST.get('signup')=='signup':
            username=""
        newuser=userSignupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully")
        else:
            print(newuser.errors)
    elif request.POST.get('signin')=='signin':
        unm=request.POST['username']
        pas=request.POST['password']


    return render(request,'index.html')

def notes(request):
    if request.method=='POST':
        mynote=notesform(request.POST,request.FILES)
        if mynote.is_valid():
            mynote.save()
            print("Your notes has been submitted!")
        else:
            print(mynote.errors)
    return render(request,'notes.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def profile(request):
    return render(request,'profile.html')