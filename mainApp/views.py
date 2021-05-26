from django.shortcuts import render, redirect
from .models import Skill

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

def skills(request):
    context = {
        "welcome": "Houston Class Project",
        'skills': Skill.objects.all().values(),
        'footer': FOOTER
    }
    return render(request, 'skills.html', context)

def addSkill(request):
    Skill.objects.create(
        skillName=request.POST['skillName']
    )
    return redirect('/skills/')