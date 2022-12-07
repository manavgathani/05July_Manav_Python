
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from myproductapp import models
from myproductapp import forms
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method=='POST':
        if request.POST.get('adminlogin') == 'adminlogin':
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('adminproduct')
            else:
                print(user.errors)
        elif request.POST.get('login') == 'login':
            email = request.POST['email']
            password = request.POST['password']
            productuser = models.Product_manager.objects.filter(email=email, password=password)
            if productuser:
                
                return redirect('searchproduct')
            else:
                print("ok to login unsussesfully")
              
    return render(request, 'homepage.html')

def adminhtml(request):
    data = models.Product_sub_cat.objects.all()
    return render(request, 'product_sub_category_details.html',{'data':data})

def deletedata(request, stid):
    id = models.Product_sub_cat.objects.get(id=stid)
    models.Product_sub_cat.delete(id)
    return redirect('adminproduct')

def updatedata(request, stid):
    id = models.Product_sub_cat.objects.get(id=stid)
    if request.method == 'POST':
        updateuser=forms.userForm(request.POST)
        if updateuser.is_valid():
            updateuser=forms.userForm(request.POST, request.FILES,instance=id)
            updateuser.save()
            print("Your records has been updated!")
            return redirect('adminproduct')
        else:
            print(updateuser.errors)
    return render(request,'updatedata.html',{'stdata':models.Product_sub_cat.objects.get(id=stid)})



def adminadddata(request):
    form = forms.ProductForm()
    
    if request.method == 'POST':
        if request.POST.get('addproduct') == 'addproduct':
            form = forms.ProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('adminproduct')
            else:
                form =  forms.ProductForm()
         
        
        elif request.POST.get('productof') == 'productof':
            productname = request.POST['productname']
            if models.Product_mst.objects.filter(productname=productname).exists():
                messages.warning(request, 'Product is already exists')
                return redirect('adminadddata')
            else:
                user = models.Product_mst(productname=productname)
                if user:
                    user.save()
                    print("ok")
                    return redirect('adminproduct')
                else:
                    print(user.errors)
                    
    return render(request,'adminadd.html',{"form":form})


def signup(request):
    form =  forms.productmanager()
    if request.method == 'POST':
        signform = forms.productmanager(request.POST)
        if signform.is_valid():
            signform.save()
            return redirect('searchproduct')
        else:
            print(signform.errors)
            
    return render(request, 'signup.html',{"form":form})

def searchproduct(request):
     if request.method == 'GET':
        query = request.GET.get('query')
        user = request.POST.get('query')
        
        if query:
            products = models.Product_mst.objects.filter(productname__icontains=query)
             
            return render(request, 'searchproduct.html', {'productsof':products})
        else:
            print("No information to show")
            return render(request, 'searchproduct.html', {})
    