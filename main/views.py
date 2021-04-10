from django.shortcuts import render
from django.http import HttpResponse
from .models import switch

# Create your views here.
def index(request):
    base=[]
    if request.method=="POST":
        #print(response.POST)
        if request.POST.get("switch_state"):
            
            data=switch()
            data.switch_state=request.POST.get("switch_state")
            data.save()

            #if response.POST.get("switch1")=="ON":
            #    base.switch_state1=True
            #else :
            #    base.switch_state1=False
            #base.save()


    return render(request,"main/base.html" , {})
    #HttpResponse("<h1>siema eniu</h1>")