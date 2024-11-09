from django.shortcuts import render,redirect
from .models import Student,Student_feedback
from django.contrib import messages
from django.views import View

#CLASS BASED VIEW FOR LOGIN FUNCTION
class Login(View):
    def get(self,request):
        return render(request,'myapp/html/login.html')
    def post(self,request):
        s_id=request.POST["userid"]
        s_pass=request.POST["userpassword"]
        
        msg=self.checkpass(s_pass)
        if msg:
            messages.error(request,msg)
            return render(request,"myapp/html/login.html")
        else:
            studnet_list=Student.objects.filter(student_id=s_id,student_password=s_pass) #select * from studnet where student_id=s_id,student_pass=s_pass)
            length=len(studnet_list)
            if length>0:
                request.session["student_key"]=s_id 
            # request.session["role"]="student"

                return redirect("student_home")
        #
#             # return render(request,"myapp/student/student_home.html")
            else:
                messages.error(request,"Invalid Credentials.")
                return render(request,"myapp/html/login.html")
        
    def checkpass(self,password):
        if len(password)<=5:
            return "PASSWORD MUST BE GREATER THAN 5 CHARACTERS"

# def login(request):

#     if request.method=='GET':
#         return render(request,'myapp/html/login.html')
#     if request.method=='POST':
#         s_id=request.POST["userid"]
#         s_pass=request.POST["userpassword"]
#         studnet_list=Student.objects.filter(student_id=s_id,student_password=s_pass) #select * from studnet where student_id=s_id,student_pass=s_pass)
#         length=len(studnet_list)
#         if length>0:
#             request.session["student_key"]=s_id 
#             # request.session["role"]="student"

#             return redirect("student_home")
#         #
#             # return render(request,"myapp/student/student_home.html")
#         else:
#             messages.error(request,"Invalid Credentials.")
#             return render(request,"myapp/html/login.html")
        
def show_home(request):
    stud_id=request.session["student_key"]
    # print(stud_id)
    # if stud_id==None:
    #     pass
    student_obj=Student.objects.get(student_id=stud_id) #getting the requierd record
    student_dict={"student_data":student_obj}  #binding record with key in dictionary
    return render(request,'myapp/student/student_home.html',student_dict)  #sending dictionary

def logout(request):
    del request.session["student_key"]
    return redirect("login")

def student_edit_profile(request):
    if request.method=="GET":
        stud_id=request.session["student_key"]
        student_obj=Student.objects.get(student_id=stud_id)
        student_dict={"student_data":student_obj}
        return render(request,'myapp/student/student_editprofile.html',student_dict)
    if request.method=="POST":
        s_email=request.POST["useremail"]
        s_phone=request.POST["userphone"]
        s_add=request.POST["useraddress"]
        s_id=request.session["student_key"]
        student_obj=Student.objects.get(student_id=s_id)
        student_obj.email=s_email
        student_obj.phone=s_phone
        student_obj.address=s_add
        student_obj.save()
        student_dict={"student_data":student_obj}
        return render(request,'myapp/student/student_home.html',student_dict)
    
def student_feedbackrating(request):
    if request.method=="GET":
        s_id=request.session["student_key"]
        student_obj=Student.objects.get(student_id=s_id)
        student_dict={"student_data":student_obj}
        return render(request,'myapp/student/student_feedback.html',student_dict)
    if request.method=="POST":
        s_feedback=request.POST["studentfeedback"]
        s_rating=request.POST["studentrating"]
        s_id=request.session["student_key"]
        student_obj=Student.objects.get(student_id=s_id)

        # student_object=Student_feedback.objects.get(student_id=student_obj)
        student_object_list=Student_feedback.objects.filter(student_id=student_obj)
        if student_object_list:   #means present in the table
            s_dict={"student_data":student_obj}
            messages.info(request,"You have already given feedback")
            return render(request,'myapp/student/student_home.html',s_dict)
        else:
            sf=Student_feedback(student=student_obj,feedback_text=s_feedback,rating=s_rating)
            sf.save()
            s_dict={"student_data":student_obj}
            messages.success(request,"Thankyou so much for your valuable feedback.")
            return render(request,'myapp/student/student_home.html',s_dict)

