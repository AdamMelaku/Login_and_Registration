from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from django.contrib import messages
from django.utils.dateparse import parse_date
# Views that make templates.


def index(request):
    return render(request,'main/index.html')

def dashboard(request):
    context = {
    "user": User.objects.get(id=request.session["user_id"]),
    "date": datetime.now(),
    "appointments_today": Appointment.objects.all(id=request.session['user_id'], date=datetime.now()),
    "upcoming_appointment": Appointment.objects.all(id=request.session['user_id']).exclude(date=datetime.now())
    }
    return render(request,'main/dashboard.html',context)

def logout(request):
	request.session.clear()
	return redirect('/')

def update_appoitment(request):
    return render(request,'main/appointments_update.html')


#Views that process forms
def login_user(request):
	if request.method == 'POST':
		login = User.objects.login_user(request.POST)
		if login:
			request.session['user_id'] = login[1].id
			return redirect('/appointments')
		else:
			messages.error(request, 'Error: Invalid credentials')
	return redirect('/')

def register_user(request):
    if User.objects.validate_user(request.POST):
        date_str = request.POST.get("date_of_birth")
        user = User.objects.create(
        name = request.POST.get("name"),
        email = request.POST.get("email"),
        date_of_birth = parse_date(date_str),
        password = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt()),
        )
        request.session["user_id"]=user.id
        return redirect("/appointments")
    messages.error(request, "Error: Invalid Login Credentials")
    return redirect("/")

def delete(request,id):
    appointment = Appointment.objects.get(id = id).delete
    return redirect ("/appointments")



# def add_appointment(request):
#     if Appointment.objects.validate_appointment(request.POST):
#         appointment = Appointment.objects.create(
#         date = request.POST.get("date"),
#         time = request.POST.get("time"),
#         task = request.POST.get("task")
#         )
