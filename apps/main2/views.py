from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.core.urlresolvers import reverse
import bcrypt
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def success(request):
    return render(request,'main/success.html')

def login_user(request):
    print "testing code"
    login = User.objects.login_user(request.POST)
    if login:
        request.session["user_id"] = login[1].id
        return redirect("/success")
    return redirect("/")

def process(request):
    if User.objects.validate_user(request.POST):
        user = User.objects.create(
        first_name = request.POST.get("first_name"),
        last_name = request.POST.get("last_name"),
        email = request.POST.get("email"),
        password = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt()),
        )
        request.session["user_id"]=user.id
        return redirect("/success")
    return redirect("/")







    # if User.UserManager.isValidEmail(request.POST['email']):
    #     encypted_password = bcrypt.hashpw(reqeust.POST["password"],bcrypt.gensalt())
    #     User.UserManager.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"],email=request.POST['email'],password=encypted_password)
    #     messages.success(request, 'The email address you entered ' + request.POST['email']+ ' is a VALID email address! and your encrypted password is '+encypted_password +'Thank you!')
    #     return redirect (reverse('success'))
    # else:
    #     messages.warning(request, 'Invalid email!')
    #     return redirect (reverse('index'))

# def success(request):
#     if request.POST["Password"]==
#     context = {
#         "User": User.UserManager.all()
#     }
#     return render(request, 'main/success.html', context)
