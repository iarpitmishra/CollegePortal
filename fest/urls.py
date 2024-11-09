from django.urls import path
from . import views
urlpatterns=[
    path("",views.fest_home,name="fest_home"),
    path("about/",views.about,name="about")


]