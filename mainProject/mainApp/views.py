from django.shortcuts import render

def index(request):
    context = {
        "welcome": "Houston Class Project"
    }
    return render(request, 'index.html', context)

def jquery(request):
    return render(request, "jQuery.html")