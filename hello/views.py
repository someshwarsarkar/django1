from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def about(request):
	n=request.POST.get("name")
	e=request.POST.get("email")
    # return HttpResponse('Hello from Python!')
	return render(request, "about.html")

def notification(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "notification.html")

def contact(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "contact.html")
def add_product(request):
	return render(request, "add_product.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
