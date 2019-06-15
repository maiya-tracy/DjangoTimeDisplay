from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime
import random

def returnRandomNumber(low, high):
    randomNumber = random.randint(low, high+1)
    return randomNumber

def addToSessionActivities(request, message, gorb):
    if not "activities" in request.session:
        request.session["activities"] = []
    message_arr = [gorb, message]
    request.session["activities"].insert(0,message_arr)

def addToTotalGold(request, amount):
    if not "total_gold" in request.session:
        request.session["total_gold"] = amount
    else:
        request.session["total_gold"] += amount
    return amount

def index(request):
    print(returnRandomNumber(-10,20))
    print("*****")
    return render(request, 'index.html')

def process_gold(request, location):
    if request.method == "POST":
        if location == "farm":
            earnings = returnRandomNumber(10,20)
            addToSessionActivities(request, "Earned " + str(earnings) + " golds from the farm! " + str(datetime.now()), "good")
        elif location == "cave":
            earnings = returnRandomNumber(5,10)
            addToSessionActivities(request, "Earned " + str(earnings) + " golds from the cave!" + str(datetime.now()), "good")
        elif location == "house":
            earnings = returnRandomNumber(2,5)
            addToSessionActivities(request, "Earned " + str(earnings) + " golds from the house!" + str(datetime.now()), "good")
        elif location == "casino":
            earnings = returnRandomNumber(-50,50)
            if earnings >=0:
                addToSessionActivities(request, "Earned " + str(earnings) + " golds from the house!" + str(datetime.now()), "good")
            else:
                addToSessionActivities(request, "Entered a casino and lost " + str(earnings) + " golds... Ouch!" + str(datetime.now()), "bad")
        addToTotalGold(request, earnings)
        return redirect('/ninja_gold/')

def clear(request):
    request.session.clear()
    return redirect ("/ninja_gold")
