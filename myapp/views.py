from django.shortcuts import render
from .models import Course,Notice,Employee,Contact,Feedback_Rating,Event
from django.contrib import messages
# Create your views here.
def index(request):
    notice_list=Notice.objects.all()
    event_list=Event.objects.all()
    notice_context={
        "notice_key":notice_list,
        "event_key":event_list
    }
    
    
    return render(request,"myapp/html/index.html",notice_context)


def about(request):
    return render(request,"myapp/html/about_us.html")

def contact(request):
    if request.method=="GET":
        return render(request,"myapp/html/contact_us.html")
    if request.method=="POST":
        u_name=request.POST["username"]   #request.POST is a built in dictionary 
        # print(uname)
        u_email=request.POST["useremail"]
        u_phone=request.POST["userphone"]
        u_query=request.POST["userquery"]
        contact_obj=Contact(name=u_name,email=u_email,phone=u_phone,user_query=u_query)
          #object creation of contact model
        contact_obj.save()
        messages.success(request,"Thankyou for contacting us !! We will soon reach you.")
        return render(request,"myapp/html/contact_us.html")

def feedback(request):
    if request.method=="GET":
        return render(request,"myapp/html/feedback.html")
    if request.method=="POST":
        u_name=request.POST["username"]   #request.POST is a built in dictionary 
        # print(uname)
        u_email=request.POST["useremail"]
        u_feedback=request.POST["userfeedback"]
        u_rating=request.POST["userrating"]
        feedback_obj=Feedback_Rating(name=u_name,email=u_email,feedback_text=u_feedback,rating=u_rating)
          #object creation of contact model
        feedback_obj.save()
        messages.success(request,"Thankyou so much for your valuable feedback.")
        return render(request,"myapp/html/feedback.html")

def courses(request):
    course_list=Course.objects.all()
    course_context={
        "course_key":course_list
    }
    return render(request,"myapp/html/courses.html",course_context)



def employee(request):
    emp_list=Employee.objects.all()
    emp_context={
        "emp_key":emp_list
    }
    return render(request,"myapp/html/employee_details.html",emp_context)