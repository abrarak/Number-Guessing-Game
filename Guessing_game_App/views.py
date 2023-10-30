from django.shortcuts import render 
from django.http import HttpResponse ,HttpResponseRedirect
import random


rand=random.randint(1,101)

def Home(request):
    return render(request , "homepage.html")
def entry(request):
    return render(request , "entry.html")
def gamewelcome(request):
    if request.method=="GET":
        return render(request,"gamewelcome.html")
    else:
        return HttpResponse("Error")
def gamecheck(request):
    if request.method=="GET":
        print(rand)
        g_number=int(request.GET["guessednumber"])
        if(g_number==rand):
                context={"guessednumber":g_number ,"randomnumber":rand}
                return render(request,"gamecheck.html",context)
        elif(g_number>rand): 
                context={"guessednumber":g_number ,"randomnumber":rand}
                return render(request,"gamecheck.html",context)
        else:
                context={ "guessednumber":g_number ,"randomnumber":rand}
                return render(request,"gamecheck.html",context)
    else:
        return HttpResponse("Error")
  
           
    
             
      

    

"""


        print(randomnumber)
  while(chance>0):
            guessed_number=int( input("Enter your number : ") )
            chance=chance-1
            if(guessed_number==randomnumber):
                print("Congratulations , You Won !!")
                break
            else:
                if(guessed_number>randomnumber):
                    print("You guessed too high !")
                    if(chance>0):
                        print(f"You have {chance} left")
                    else:
                        pass
                else:
                    print("You guessed too low !")
                    if(chance>0):
                       print(f"You have {chance} left")
                    else:
                       pass
        else:
            print("Sorry ! You have no more chance")
       
      
"""

