from django.shortcuts import render, redirect
from .models import *

def officialZoo(request):
    return render(request, 'officialZoo.html')


# Landing page to view zoos
def allZoos(request):
    context = {
        'allZoos': Zoo.objects.all().values()
    }
    return render(request, 'allZoos.html', context)

# Hidden route to create Zoo
def createZoo(request):
    if request.method == "GET":
        return redirect('/zoo/createZoo/')
    Zoo.objects.create(
        zooName=request.POST['zooName'],
        zooLocation=request.POST['zooLocation']
    )
    return redirect('/zoo/theZoos/')

# Landing page to edit 1 zoo
def editZoo(request, zoo_id):
    oneZoo = Zoo.objects.get(id=zoo_id)
    context = {
        'editZoo': oneZoo
    }
    return render(request, 'editZoo.html', context)

# Hidden route to update zoo
def updateZoo(request, zoo_id):
    toUpdate = Zoo.objects.get(id=zoo_id)
    toUpdate.zooName = request.POST['zooName']
    toUpdate.zooLocation = request.POST['zooLocation']
    toUpdate.save()

    return redirect('/zoo/theZoos/')

# Hidden route to delete zoo
def deleteZoo(request, zoo_id):
    toDelete = Zoo.objects.get(id=zoo_id)
    toDelete.delete()

    return redirect('/zoo/theZoos/')

# Landing page to view all Animals
def allAnimals(request):
    context = {
        'allZoos': Zoo.objects.all().values(),
        'allAnimals': Animal.objects.all().values()
    }
    return render(request, 'allAnimals.html', context)

# Hidden route to create Animal
def createAnimal(request):
    if request.method == "GET":
        return redirect('/zoo/createAnimal/')
    animalZoo = Zoo.objects.get(id = request.POST['zoo_id'])
    Animal.objects.create(
        animalName=request.POST['animalName'],
        animalType=request.POST['animalType'],
        animalBirth=request.POST['animalBirth'],
        animalZoo=animalZoo
    )
    return redirect('/zoo/theAnimals/')

# Landing page to edit 1 animal
def editAnimal(request, animal_id):
    oneAnimal = Animal.objects.get(id=animal_id)
    context = {
        'editAnimal': oneAnimal,
        'allZoos': Zoo.objects.all().values(),
    }
    return render(request, 'editAnimal.html', context)

# Hidden route to update zoo
def updateAnimal(request, animal_id):
    toUpdate = Animal.objects.get(id=animal_id)
    toUpdate.animalName = request.POST['animalName']
    toUpdate.animalType = request.POST['animalType']
    toUpdate.animalBirth = request.POST['animalBirth']
    toUpdate.zoo_id = request.POST['zoo_id']
    toUpdate.save()

    return redirect('/zoo/theAnimals/')

# Hidden route to delete zoo
def deleteAnimal(request, zoo_id):
    toDelete = Animal.objects.get(id=animal_id)
    toDelete.delete()

    return redirect('/zoo/theAnimals/')