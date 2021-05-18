from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def officialZoo(request):
    return render(request, 'officialZoo.html')


# Landing page to view zoos
def allZoos(request):
    context = {
        'zoos': Zoo.objects.all()
    }
    return render(request, 'allZoos.html', context)

# Hidden route to create Zoo
def createZoo(request):
    if request.method == "GET":
        return redirect('/zoo/createZoo/')
    Zoo.objects.create(
        zooName=request.POST['zooName'],
        zooLocation=request.POST['zooLocation'],
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
        'zoos': Zoo.objects.all()
    }
    return render(request, 'allAnimals.html', context)

# Hidden route to create Animal
def createAnimal(request):
    if request.method == "GET":
        return redirect('/zoo/createAnimal/')
    Animal.objects.create(
        animalName=request.POST['animalName'],
        animalType=request.POST['animalType'],
        animalBirth=request.POST['animalBirth'],
        zoo_id=request.POST['zoo'],
    )
    return redirect('/zoo/theAnimals/')

# Landing page to edit 1 animal
def editAnimal(request, animal_id):
    oneAnimal = Animal.objects.get(id=animal_id)
    context = {
        'editAnimal': oneAnimal,
        'zoos': Zoo.objects.all().values(),
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

# Hidden route to delete animal
def deleteAnimal(request, animal_id):
    toDelete = Animal.objects.get(id=animal_id)
    toDelete.delete()

    return redirect('/zoo/theAnimals/')

# Landing page to view all Employee's
def allEmployees(request):
    context = {
        'zoos': Zoo.objects.all()
    }
    return render(request, 'allEmployees.html', context)

# Hidden route to create Employee
def createEmployee(request):
    if request.method == "GET":
        return redirect('/zoo/createEmployee/')
    Employee.objects.create(
        firstName=request.POST['firstName'],
        lastName=request.POST['lastName'],
        email=request.POST['email'],
        zoo_id=request.POST['zoo'],
    )
    return redirect('/zoo/theEmployees/')

# Landing page to edit 1 Employee
def editEmployee(request, employee_id):
    oneEmployee = Employee.objects.get(id=employee_id)
    context = {
        'editEmployee': oneEmployee,
        'zoos': Zoo.objects.all().values(),
    }
    return render(request, 'editEmployee.html', context)

# Hidden route to update Employee
def updateEmployee(request, employee_id):
    toUpdate = Employee.objects.get(id=employee_id)
    toUpdate.firstName = request.POST['firstName']
    toUpdate.lastName = request.POST['lastName']
    toUpdate.email = request.POST['email']
    toUpdate.zoo_id = request.POST['zoo_id']
    toUpdate.save()

    return redirect('/zoo/theEmployees/')

# Hidden route to delete zoo
def deleteEmployee(request, employee_id):
    toDelete = Employee.objects.get(id=employee_id)
    toDelete.delete()

    return redirect('/zoo/theEmployees/')

# Landing page for Shows
def show(request):
    # if request.method == 'post':
    #     errors = Show.objects.validate(request.POST)
    #     if errors:
    #         for err in errors.values():
    #             messages.error(request, err)
    #         return redirect('/zoo/theShows/')
    context = {
        'zoos': Zoo.objects.all()
    }
    return render(request, 'allShows.html', context)

# Hidden route to create new show
def createShow(request):
    errors = Show.objects.validate(request.POST)
    if errors:
        for err in errors.values():
            messages.error(request, err)
        return redirect('/zoo/theShows/')
    Show.objects.create(
        showName=request.POST['showName'],
        zoo_id=request.POST['zoo'],
    )
    return redirect('/zoo/theShows/')