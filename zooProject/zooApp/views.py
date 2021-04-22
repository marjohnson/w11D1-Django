from django.shortcuts import render, HttpResponse, redirect

PLACES = (
    'Berwick',
    'Houston'
)

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

def test(request):
    return render(request, "test.html")

# Without Sessions and Redirect

# def form(request):
#     return render(request, "zooForm.html")
#     # if request.method == "GET":
#     #     print("GET request was made for zooForm.html")
#     #     return render(request, "zooForm.html")
#     # if request.method == "POST":
#     #     print("POST request was made for zooForm.html")

# def results(request):
#     if request.method == "POST":
#         context = {
#             'memberName': request.POST['memberName'],
#         }
#         return render(request, 'results.html', context)
#     return render(request, 'results.html')

def form(request):
    return render(request, 'zooForm.html')

def newMembers(request):
    if request.method == 'GET':
        return redirect('/form/')
    request.session['results'] = {
        'memberName': request.POST['memberName'],
    }
    return redirect('/results')

def results(request):
    context = {
        'results': request.session['results'],
    }
    return render(request, 'results.html', context)