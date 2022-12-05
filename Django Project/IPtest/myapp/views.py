from django.shortcuts import render, redirect
from .forms import userform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import user

# Create your views here.
@login_required(login_url='login')
def index(request):
    data = user.objects.all()
    uid = request.session.get('uid')
    return render(request, 'index.html',{'data':data, 'cid':user.objects.get(id=uid)})

def login(request):
    if request.method == 'POST':
        useremail = request.POST['email']
        usercity = request.POST['city']
        usermod = user.objects.filter(email=useremail, city=usercity)
        uid = user.objects.get(email=useremail)
        if usermod:
            print("login done")
            request.session['email']=useremail
            request.session['uid'] = uid.id
            
            return redirect('index')
        else:
            print(usermod.errors)
    return render(request, 'login.html')

def updatadat(request, stid):
    id = user.objects.get(id=stid)
    if request.method == 'POST':
        updatauser = userform(request.POST)
        if updatauser.is_valid():
            updatauser = userform(request.POST, instance=id)
            updatauser.save()
            return redirect('index')
        else:
            print(updatauser.errors)
    return render(request, 'updatadat.html',{'stdata':user.objects.get(id=stid)})

def useradd(request):
    if request.method == 'POST':
        userdata = userform(request.POST)
        if userdata.is_valid():
            userdata.save()
            return redirect('login')
        else:
            print(userform.errors)
    return render(request, 'useradd.html')

def deletedata(request, stid):
    id = user.objects.get(id=stid)
    
    user.delete(id)
    return redirect('index')

def userlogout(request):
    logout(request)
    return redirect("login")

def searchname(request):
     if request.method == 'GET':
        query = request.GET.get('query')
        
        
        if query:
            username = user.objects.filter(name__icontains=query)
             
            return render(request, 'searchname.html', {'usernameof':username})
        else:
            print("No information to show")
            return render(request, 'searchname.html', {})