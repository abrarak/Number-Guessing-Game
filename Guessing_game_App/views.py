from django.shortcuts import render
from .models import info
from django.http import HttpResponse
import random 

# Create your views here.
def home(request):
    return render(request , "homepage.html")
def guess(request):
    context={"chance":7}
    return render(request,"guess.html", context)
def number(request):
    if request.method=="POST":
        username=request.POST["username"]
        number=request.POST["number"]
        chance=7
        randonumber=random.randint(1,100)
        u_name=info(username=username, usernumber=number,systemnumber=randonumber , chance=chance)
        u_name.save()
        context={"username":username,"number":number ,"chance":chance}
        return render(request,"number.html",context)
    else:
         return HttpResponse("Error")
def validate(request):
    if request.method=="POST":
        chance=info.objects.values().latest("id")["chance"]
        chance=chance-1
        usernumber=info.objects.values().latest("id")["usernumber"]
        username=info.objects.values().latest("id")["username"]
        systemnumber=info.objects.values().latest("id")["systemnumber"]
        usernumber=info.objects.values().latest("id")["usernumber"]
        u_name=info(username=username, usernumber=usernumber,systemnumber=systemnumber, chance=chance)
        u_name.save()
        context={"username":username , "systemnumber":systemnumber,"usernumber":usernumber,"chance":chance}
        return render(request,"validate.html",context)
    else:
         return HttpResponse("Error")
def retry(request):
        chance=info.objects.values().latest("id")["chance"]
        chance=chance-1
        usernumber=info.objects.values().latest("id")["usernumber"]
        username=info.objects.values().latest("id")["username"]
        systemnumber=info.objects.values().latest("id")["systemnumber"]
        usernumber=info.objects.values().latest("id")["usernumber"]
        u_name=info(username=username, usernumber=usernumber,systemnumber=systemnumber, chance=chance)
        u_name.save()
        context={"username":username , "systemnumber":systemnumber,"usernumber":usernumber,"chance":chance}
        return render(request,"retry.html",context)
def validateretry(request):
    if request.method=="POST":
        number=request.POST["number"]
        chance=info.objects.values().latest("id")["chance"]
        username=info.objects.values().latest("id")["username"]
        systemnumber=info.objects.values().latest("id")["systemnumber"]
        u_name=info(username=username, usernumber=number,systemnumber=systemnumber, chance=chance)
        u_name.save()
      
        usernumber=info.objects.values().latest("id")["usernumber"]
        context={"username":username , "systemnumber":systemnumber,"usernumber":usernumber ,"chance":chance}
        return render(request,"validate.html",context)
    else:
         return HttpResponse("Error")




