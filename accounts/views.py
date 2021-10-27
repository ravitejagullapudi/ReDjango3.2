from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


# Create your views here.
def login_view(request):
    if(request.method=="POST"):
        form =AuthenticationForm(request,data=request.POST)
        # username = request.POST['username']
        # password = request.POST['password']
        # # print(username,password)
        # user = authenticate(request,username=username, password=password)
        # if user is None:
        #     context = {"error":"Invalid username or password"}
        #     return render(request,'accounts/login.html',context)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/')
    else:
        form =AuthenticationForm(request)
    return render(request,'accounts/login.html',{"form":form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
    return render(request,'accounts/logout.html',{})

def register_view(request):
    form  =  UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        return redirect('/login')
    return render(request, "accounts/register.html",{"form":form})

