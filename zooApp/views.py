from django.shortcuts import render, HttpResponse, redirect
import random
from .models import Animals

# These are our categories and their min/max ticket prices
TICKETS = {
    "souvenirs": (4,9),
    "food": (2,7),
    "tShirts": (10,20),
    "stuffedAnimals": (5,15),
}

FOOTER = {
    'Created by Amazon Career Choice Houston Class',
    '© 2021'
}

# main landing page
def zoo(request):
    context = {
        "zooName": "Ninja Zoo",
        "zooLocation": "H-Town, TX",
        "zooAnimals": ["Giraffes", "Tigers", "Bears", "Penguins"],
        'footer': FOOTER
    }
    return render(request, "zoo.html", context)
    
# the rest was built and migrate was done before testing

# main form page to add new member
def form(request):
    context = {
        'footer': FOOTER
    }
    return render(request, 'zooForm.html', context)

# route to actually add a new member
def newMembers(request):
    if request.method == 'GET':
        return redirect('zooApp/form/')
    request.session['results'] = {
        'memberName': request.POST['memberName'],
    }
    return redirect('/zooApp/results')

# the page that displays the information entered on the new member form
def results(request):
    context = {
        'results': request.session['results'],
        'footer': FOOTER
    }
    return render(request, 'results.html', context)

# The main Ninja Shop page showing current total earned by the shop and with the options to purchase items and add to that total
def theShop(request):
    if not "price" in request.session:
        request.session['price'] = 0
    context = {
        'footer': FOOTER
    }
    return render(request, 'theNinjaShop.html', context)

# clear shop total earned
def reset(request):
    request.session.clear()
    return redirect('/zooApp/the-shop')

# route to actually add to our total
def purchase(request):
    if request.method == 'GET':
        return redirect('/zooApp/the-shop/')
    
    itemName = request.POST['categories']
    categories = TICKETS[itemName]

    currTotal = random.randint(categories[0], categories[1])

    result = 'total'

    request.session['price'] += currTotal
    return redirect('/zooApp/the-shop/')

# Display our newly added Animals
def animals(request):
    context = {
        "allAnimals": Animals.objects.all().values()
    }
    return render(request, 'animals.html', context)

def addAnimal(request):
    return render(request, 'newAnimals.html')

def create(request):
    if request.method == 'GET':
        return redirect('zooApp/addAnimal/')
    Animals.objects.create(
        animalName=request.POST['animalName'],
        animalType=request.POST['animalType'],
        animalBirth=request.POST['animalBirth']
    )

    return redirect('/zooApp/animals/')