from django.shortcuts import render, HttpResponse

def index(request):
    context = {
        "zooName": "Ninja Zoo",
        "zooLocation": "H-Town, TX",
        "zooAnimals": ["Giraffes", "Tigers", "Bears", "Penguins"]
    }
    return render(request, "index.html", context)

def about(request):
    return HttpResponse("About our Project/Application")

def contributors(request):
    return HttpResponse("This will show who contributed to the project and application")
