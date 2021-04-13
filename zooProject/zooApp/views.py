from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome our Zoo Database")

def about(request):
    return HttpResponse("About our Project/Application")

def contributors(request):
    return HttpResponse("This will show who contributed to the project and application")
