from django.shortcuts import render

FOOTER = {
    'Created by Amazon Career Choice Houston Class',
    '© 2021'
}

def index(request):
    context = {
        "welcome": "Houston Class Project",
        'footer': FOOTER
    }
    return render(request, 'index.html', context)

def jquery(request):
    return render(request, "jQuery.html")