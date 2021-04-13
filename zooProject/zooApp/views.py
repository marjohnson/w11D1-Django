from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome our Zoo Database")

def about(request):
    return HttpResponse("All about our Database")
