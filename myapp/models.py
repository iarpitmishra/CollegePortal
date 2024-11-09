from django.db import models
from django.utils import timezone

# Create your models here.
class Notice(models.Model):
    notice_contents=models.CharField(max_length=45)
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.notice_contents

class Course(models.Model):
    course_name=models.CharField(max_length=45,primary_key=True)
    course_fees=models.IntegerField()
    course_duration=models.CharField(max_length=40)
    course_contents=models.TextField(blank=True)
    def __str__(self):
        return self.course_name

class Contact(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField(max_length=45)
    phone=models.CharField(max_length=10)
    user_query=models.TextField()
    date=models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.name
    
class Feedback_Rating(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField(max_length=45)
    feedback_text=models.TextField()
    rating=models.CharField(max_length=6)
    date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=45)
    email=models.EmailField(max_length=45)
    phone=models.CharField(max_length=10)
    designation=models.CharField(max_length=45)
    employee_pic=models.FileField(max_length=200,upload_to="myapp/employee_pic",default="")

    def __str__(self):
        return self.name

class Event(models.Model):
    event_name=models.CharField(max_length=50)
    event_venue=models.CharField(max_length=100)
    event_pic=models.FileField(max_length=100,upload_to="myapp/event_pic",default="")
    event_description=models.TextField()
    event_date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.event_name
    
gender=[
    ("M","Male"),
    ("F","Female")
]

class Student(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    name=models.CharField(max_length=45)
    email=models.EmailField(max_length=45)
    phone=models.CharField(max_length=10)
    student_id=models.CharField(max_length=40,primary_key=True)
    student_password=models.CharField(max_length=40)
    gender=models.CharField(max_length=6,choices=gender)
    description=models.TextField()
    address=models.TextField()
    student_pic=models.FileField(max_length=200,upload_to="myapp/student_pic",default="")

    def __str__(self):
        return self.name
    
    
class Consultancy(models.Model):
    c_id=models.CharField(max_length=40,primary_key=True)
    c_password=models.CharField(max_length=40)
    c_name=models.CharField(max_length=45)
    c_phone=models.CharField(max_length=10)
    c_email=models.EmailField(max_length=45)
    c_description=models.TextField()
    date=models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.c_name
    
class Student_feedback(models.Model):
    student=models.OneToOneField(Student,on_delete=models.DO_NOTHING)
    feedback_text=models.TextField()
    rating=models.CharField(max_length=6)
    date=models.DateField(default=timezone.now)
