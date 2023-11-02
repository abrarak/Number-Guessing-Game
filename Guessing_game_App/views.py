from django.shortcuts import render
from .models import username,userrangeandchance,usernumber
from django.http import HttpResponse
import random 
from math import log2

# Create your views here.
def home(request):
    return render(request , "1_homepage.html")
def usernameentry(request):
    return render(request , "2_usernameentry.html")
def rangeentry(request):
    if request.method=="POST":
        username_input=request.POST["username"]
        u_name=username(user_name = username_input)
        u_name.save()
        context={"username":username_input}
        return render(request,"3_rangeentry.html",context)
    else:
         return HttpResponse("Error")
def numberentry(request):
    if request.method=="POST":
        l1=int(request.POST["lowerrange"])
        l2=int(request.POST["upperrange"])
        c=int(log2(l2-l1)+1)
        randomnumber=random.randint(l1,l2)
        u_range=userrangeandchance(lowerrange=l1,upperrange=l2,chance=c,systemnumber=randomnumber)
        u_range.save()
        context={"lowerrange":l1,"upperrange":l2,"chance":c}
        return render(request,"3_showrangeandchance.html",context)
    else:
         return HttpResponse("Error")
    
def validate(request):
    if request.method=="POST":
        u_number=int(request.POST["unum"])
        unumber=usernumber(usernumber=u_number)
        unumber.save()
        u_name=username.objects.values().latest("id")["user_name"]
        systemnumber=userrangeandchance.objects.values().latest("id")["systemnumber"]
        chance=userrangeandchance.objects.values().latest("id")["chance"]
        print(systemnumber)
        l1=userrangeandchance.objects.values().latest("id")["lowerrange"]
        l2=userrangeandchance.objects.values().latest("id")["upperrange"]
        chance=chance-1
        
        range_s=userrangeandchance(systemnumber=systemnumber, chance=chance ,lowerrange=l1,upperrange=l2)
        range_s.save()
        context={"username":u_name , "systemnumber":systemnumber,"usernumber":u_number,"chance":chance}
        return render(request,"validate.html",context)
    else:
         return HttpResponse("Error")