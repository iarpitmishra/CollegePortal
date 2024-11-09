from django.shortcuts import render
from .models import Consultancy
from django.contrib import messages

def registration(request):
    if request.method=="GET":
        return render(request,"myapp/consultancy/c_registration.html")
    if request.method=="POST":
        id=request.POST["c_id"] 
        password=request.POST["c_password"] 
        name=request.POST["c_name"]   #request.POST is a built in dictionary 
        # print(uname)
        phone=request.POST["c_phone"] 
        email=request.POST["c_email"]
        description=request.POST["c_description"]
        consultancy_obj=Consultancy(c_id=id,c_password=password,c_name=name,c_phone=phone,c_email=email,c_description=description)
          #object creation of contact model
        consultancy_obj.save()
        messages.success(request,"Congratutations!! You have registered successfully.")
        return render(request,"myapp/consultancy/c_registration.html")