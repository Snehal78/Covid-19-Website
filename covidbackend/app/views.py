from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Contact, Register

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def symptoms(request):
    return render(request, "symptoms.html")

def vaccines(request):
    return render(request, "vaccines.html")

def registration(request):
    if request.method=="GET":
        return render(request, "registration.html")
    if request.method=="POST":
        data = request.POST
        name = data.get('name')
        surname = data.get('surname')
        email = data.get('email')
        phoneno = data.get('phoneno')
        district = data.get('district')
        pincode = data.get('pincode')
        gender = data.get('gender')
        adhaarno = data.get('adhaarno')
        Register.objects.create(name=name, surname=surname, email=email, phoneno=phoneno, district=district, pincode=pincode, gender=gender, adhaarno=adhaarno)
        return HttpResponse("<h1>User has Registered Successfully..!!</h1>")

def contact(request):
    
    if request.method=="POST":
        data = request.POST
        name = str(data.get('name'))
        email = str(data.get('email'))
        phoneno = str(data.get('phoneno'))
        symptoms = json.dumps(data.getlist('symptoms'))
        description = str(data.get('description'))
        Contact.objects.create(name=name, email=email, phoneno=phoneno, symptoms=symptoms, description=description)
        return HttpResponse("Information Received. We will Contact You Soon :)")
    if request.method=="GET":
        return render(request, "contact.html")