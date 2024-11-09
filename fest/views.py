from django.shortcuts import render,HttpResponse

# Create your views here.
def fest_home(request):
    return HttpResponse("<h1>hello fest</h1>")

def about(request):
    return HttpResponse("<h1>ABOUT US</h1>")
