from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        'caption': "Django"
    }
    return render(request, "main/index.html", data)

def new(request):
    return render(request, "main/new.html")

def page3(request):
    return render(request, "main/page3.html")

def page4(request):
    return render(request, "main/page4.html")
