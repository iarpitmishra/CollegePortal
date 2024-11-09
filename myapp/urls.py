from django.urls import path
from .import views,student_views,consultancy_views
urlpatterns = [
    path("",views.index,name="index"),
    path("about/",views.about,name="about_us"),
    path("contact/",views.contact,name="contact_us"),
    path("feedback/",views.feedback,name="feedback"),
    path("courses/",views.courses,name="courses"),

    # path("login/",student_views.login,name="login"),
    path("login/",student_views.Login.as_view(),name="login"),

    path("ourstaff/",views.employee,name="employee"),
    path("student_home/",student_views.show_home,name="student_home"),
    path("logout/",student_views.logout,name="logout"),
    path("consultancy/",consultancy_views.registration,name="registration"),
    path("student_edit_profile/",student_views.student_edit_profile,name="student_edit_profile"),
    path("student_feedback/",student_views.student_feedbackrating,name="student_feedback"),

]