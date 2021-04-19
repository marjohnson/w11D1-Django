from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html")

def about(request):
    return HttpResponse("About Melissa")

def testForm(request):
    if request.method == "GET":
        print("A GET request was made from this route")
        print(request.GET)
        return render(request, "testForm.html")
    if request.method == "POST":
        print("A POST request was made from this route")
        print(request.POST)