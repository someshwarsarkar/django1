from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")
def login(request):
    return render(request, "login.html")
def p_import(request):
    return render(request, "import.html")
def add_product(request):
    return render(request, "add_product.html")
def manage_product(request):
    return render(request, "manage_product.html")
def add_category(request):
    return render(request, "add_category.html")
def manage_category(request):
    return render(request, "manage_category.html")
def add_warehouse(request):
    return render(request, "add_warehouse.html")
def manage_warehouse(request):
    return render(request, "manage_warehouse.html")
def export(request):
    return render(request, "export.html")
def invoice(request):
    return render(request, "invoice.html")
def report(request):
    return render(request, "report.html")
def contact_us(request):
    return render(request, "contact_us.html")
def front(request):
    return render(request, "front.html")
def navbar(request):
    return render(request, "navbar.html")
def sidebar(request):
    return render(request, "sidebar.html")
def stock(request):
    return render(request, "stock.html")
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
