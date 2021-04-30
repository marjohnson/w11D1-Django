from django.shortcuts import render, HttpResponse, redirect
import random

# These are our categories and their min/max ticket prices
TICKETS = {
    "souvenirs": (4,9),
    "food": (2,7),
    "tShirts": (10,20),
    "stuffedAnimals": (5,15),
}

# main landing page
def zoo(request):
    context = {
        "zooName": "Ninja Zoo",
        "zooLocation": "H-Town, TX",
        "zooAnimals": ["Giraffes", "Tigers", "Bears", "Penguins"]
    }
    return render(request, "zoo.html", context)
    
# the rest was built and migrate was done before testing

# main form page to add new member
def form(request):
    return render(request, 'zooForm.html')

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
    }
    return render(request, 'results.html', context)

# The main Ninja Shop page showing current total earned by the shop and with the options to purchase items and add to that total
def theShop(request):
    if not "price" in request.session:
        request.session['price'] = 0
    return render(request, 'theNinjaShop.html')

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
