from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if "gold" not in request.session:
        request.session["gold"]=0
    if 'activity_log' not in request.session:
        request.session['activity_log'] = []
    return render(request,'NinjaGold/index.html')

def find_gold(request):
    if request.POST["location"]=="farm":
        value = random.randrange(10,21)
        request.session["gold"]+= value
        string = "You have earned " + str(value) + " golds from the farm. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        request.session["activity_log"].append(string)
        return redirect ("/")
    if request.POST["location"]=="cave":
        value = random.randrange(5,11)
        request.session["gold"]+= value
        string = "You have earned " + str(value) + " golds from the cave. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        request.session["activity_log"].append(string)
        return redirect ("/")
    if request.POST["location"]=="house":
        value = random.randrange(2,6)
        request.session["gold"]+= value
        string = "You have earned " + str(value) + " golds from the house. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        request.session["activity_log"].append(string)
        return redirect ("/")
    if request.POST["location"]=="casino":
        value = random.randrange(-50,51)
        request.session["gold"]+= value
        if value >=0:
            string = "You have earned " + str(value) + " golds from the casino. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
        else:
            string = "You have lost " + str(value) + " golds from the casino. " + str(datetime.now().strftime("%Y/%m/%d %I:%M%p"))
            request.session["activity_log"].append(string)
        return redirect ("/")
