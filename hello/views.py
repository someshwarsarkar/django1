from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")
def p_import(request):
    return render(request, "import.html")
def p_add(request):
    return render(request, "p_add.html")
def p_manage(request):
    return render(request, "p_manage.html")
def c_add(request):
    return render(request, "c_manage.html")
def c_manage(request):
    return render(request, "c_manage.html")
def w_add(request):
    return render(request, "w_add.html")
def w_manage(request):
    return render(request, "w_manage.html")
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
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
