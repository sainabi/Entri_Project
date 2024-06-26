from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


@login_required
def index(request):
    return render(request,'product.html')
def add(request):
    try:
        Name=request.POST['name']
        Description=request.POST['description']
        Price=int(request.POST['price'])
        Quantity=int(request.POST['quantity'])
        proobj=Product.objects.create(name=Name,description=Description,price=Price,quantity=Quantity)
        proobj.save()
        return render(request,'product.html',{"msg":"product added"})
   
    except Exception as e:
       print(e)
       return render(request, 'product.html', {"msg": "product not added"})

    
def display(request):
    prodlist=Product.objects.all()
    return render(request,'product.html',{"lists":prodlist})

def delete(request):
    delname=request.POST['name']
    deltname=Product.objects.filter(name=delname)
    if deltname.exists():
        deltname.delete()
        return render(request,'product.html',{"msg1":"product deleted"})
    else:
        return render(request,'product.html',{"msg1":"product not deleted"})
def update(request):
    try: 
       Newproduct=request.POST["newproduct"]
       Oldproduct=request.POST["oldproduct"]
       productnew=Product.objects.filter(name=Oldproduct)
       if productnew.exists():
         productnew.update(name=Newproduct)
         return render(request,'product.html',{"msg2":"Updated"})
       else:
         return render(request,'product.html',{"msg2":"price not found"})
    except Exception as e:
        print(e)
        return render(request,'product.html',{"msg2":"Not Updated"})




def sign_up(request):
     try:
        form = UserCreationForm(request.POST)
        if request.method=="POST":
            if form.is_valid():
                form.save()
                return redirect('login')
            return render(request,'sign_up.html',{'form': form,'msg':'invalid login'})
        else:
            return render(request,'sign_up.html',{'form': form,'msg':'invalid submission'})
     except Exception as e:
        print(e)
        form=UserCreationForm()
        return render(request,'sign_up.html',{'form':form})
     
def Loginpage(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request, username=uname,password=pwd)
    if user is not None:
        login(request,user)
        return redirect('index')
    else:
          return render(request,"login.html",{"msg":"invalid login"})
    
def Resethome(request):
    return render(request,'Resetpassword.html')
def resetPassword(request):
    uname = request.POST.get('uname')
    newpwd = request.POST.get('password')
    try:
        user = User.objects.get(username=uname)
        if user is not None:
            user.set_password(newpwd)
            user.save()
            return render(request, "Resetpassword.html", {"msg": "Password reset successfully"})
    except Exception as e:
        print(e)
        return render(request, "Resetpassword.html", {"msg": "Password reset failed"})

   
def Logout_view(request):
    logout(request)
    return redirect('login')