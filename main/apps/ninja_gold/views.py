from django.shortcuts import render, redirect, HttpResponse
import random, datetime


# Create your views here.
def index(request):
    if not "gold" in request.session:
        request.session["gold"] = 0
    if not "activities" in request.session:
        request.session["activities"] = []
    return render(request,"ninja_gold/index.html")

def process(request):
    if request.method == "POST":
        gold_made = 0
        print(request.POST["areaname"])
        if request.POST["areaname"] == "farm":
            gold_made = random.randint(10,20)
        elif request.POST["areaname"] == "cave":
            gold_made = random.randint(5,10)
        elif request.POST["areaname"] == "house":
            gold_made = random.randint(2,5)
        elif request.POST["areaname"] == "casino":
            gold_made = random.randint(-50,50)
        print(gold_made)
        request.session["gold"] += gold_made
        request.session["activities"].insert(0, make_string(request.POST["areaname"],gold_made))
        request.session.modified=True
        return redirect("/")
    else:
        return redirect("/")

#functions not attached to urls or routes
def make_string(area,gold):
    newstr = {}
    if gold < 0:
        gold *= -1
        gold = str(gold)
        newstr = {"id":"lost",
                "act_str":"Entered a " + area + " and lost " + gold + " golds... Ouch.. " + create_time_stamp()}
    else:
        gold = str(gold)
        newstr ={"id":"won",
                "act_str":"Earned " +  gold + " golds from the " + area + "! " + create_time_stamp()}
    return newstr

def create_time_stamp():
    now = datetime.datetime.now()
    stampstr = ""
    if(now.hour > 12):
        stampstr = "(" + str(now.year) + "/" + str(now.month) + "/" + str(now.day) + " " + str(now.hour - 12) + ":" + str(now.minute) + " PM" + ")"
    else:
        stampstr = "(" + str(now.year) + "/" + str(now.month) + "/" + str(now.day) + " " + str(now.hour) + ":" + str(now.minute) + " PM" + ")"
    return stampstr
