from django.contrib import admin
from .models import Notice,Course,Contact,Feedback_Rating,Employee,Event,Student,Consultancy,Student_feedback

class Course_Admin(admin.ModelAdmin):
    list_display=('course_name','course_fees','course_duration')
    list_filter=['course_fees','course_duration']
    search_fields=('course_name','course_fees')

class Employee_Admin(admin.ModelAdmin):
    list_display=('name','email','phone','designation')
    list_filter=['designation']
    

class Notice_Admin(admin.ModelAdmin):
    list_display=('notice_contents','date')

class Contact_Admin(admin.ModelAdmin):
    list_display=('name','email','phone')

class Event_Admin(admin.ModelAdmin):
    list_display=('event_name','event_venue','event_date')

class Student_Admin(admin.ModelAdmin):
    list_display=('course','name','email','phone')

class Consultancy_Admin(admin.ModelAdmin):
    list_display=('c_id','c_name','c_phone')


# Register your models here.
admin.site.register(Notice,Notice_Admin)
admin.site.register(Course,Course_Admin)
admin.site.register(Contact,Contact_Admin)
admin.site.register(Feedback_Rating)
admin.site.register(Employee,Employee_Admin)
admin.site.register(Event,Event_Admin)
admin.site.register(Student,Student_Admin)
admin.site.register(Consultancy,Consultancy_Admin)
admin.site.register(Student_feedback)


admin.site.site_header="CollegePortalAdminstration"
admin.site.site_title="CollegeAdmin Dashboard"
admin.site.index_title="College Admin"



