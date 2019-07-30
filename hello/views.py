from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import Product
from .models import Category

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
def add_pdt_hid(request):
    pdt_name=request.POST.get("pdt_name")
    pdt_price=request.POST.get("pdt_price")
    pdt_cat=request.POST.get("pdt_cat")
    obj=Product()
    obj.pdt_name=pdt_name
    obj.pdt_price=pdt_price
    obj.pdt_cat=pdt_cat
    obj.save()
    return render(request, "add_pdt_hid.html",{"pdt_name":pdt_name, "pdt_price":pdt_price, "pdt_cat":pdt_cat})
def manage_product(request):
    pdt=Product.objects.all()
    return render(request, "manage_product.html",{'pdt':pdt})
def add_category(request):
    return render(request, "add_category.html")
def add_cat_hid(request):
    cat_name=request.POST.get("cat_name")
    cat_gst=request.POST.get("cat_gst")
    cobj=Category()
    cobj.cat_name=cat_name
    cobj.cat_gst=cat_gst
    cobj.save()
    return render(request, "add_cat_hid.html", {"cat_name":cat_name, "cat_gst":cat_gst})
def manage_category(request):
    cat=Category.objects.all()
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
def list(request):
    return render(request, "list.html")
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
