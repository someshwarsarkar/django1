from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import Product
from .models import Category
from .models import Invoice

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")
def login(request):
    return render(request, "login.html")
def p_import(request):
    pname=Product.objects.all()
    return render(request, "import.html", {'pname':pname})
def add_product(request):
    p=Category.objects.all()
    return render(request, "add_product.html",{'p':p})
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
    return render(request, "manage_category.html", {'cat':cat})
def export(request):
    inv=Invoice.objects.all()
    return render(request, "export.html", {'inv':inv})
def invoice(request):
    p=Product.objects.all()
    return render(request, "invoice.html", {'p':p})
def invoice_hid(request):
    pname=request.POST.get("pname")
    qty=request.POST.get("qty")
    unitprice=request.POST.get("unitprice")
    cname=request.POST.get("cname")
    cnumber=request.POST.get("cnumber")
    dis=request.POST.get("dis")
    iobj=Invoice()
    iobj.pname=pname
    iobj.qty=qty
    iobj.unitprice=unitprice
    iobj.cname=cname
    iobj.cnumber=cnumber
    iobj.dis=dis
    iobj.save()
    return render(request, "invoice_hid.html", {"pname":pname, "qty":qty, "unitprice":unitprice, "cname":cname, "cnumber":cnumber, "dis":dis})
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
def delete(request):
    d_id=request.POST.get("d_id")
    pdel=Product.objects.filter(id=d_id).delete()
    return render(request, "delete.html", {"d_id":d_id})
def cat_delete(request):
    c_id=request.POST.get("c_id")
    cdel=Category.objects.filter(id=c_id).delete()
    return render(request, "cat_delete.html", {"c_id":c_id})
def print(request):
    i_id=request.POST.get("i_id")
    psel=Invoice.objects.filter(id=i_id)
    pd=Product.objects.all()
    k=0
    for i in pd:
        if (i[k]["id"]==15):
            cname=i[k]["pdt_name"]
            break
        k=k+1
    return render(request, "print.html",{"i_id":i_id, "cname":cname})
def lc(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    return render(request, "lc.html", {"username":username, "password":password})
def logout(request):
    return render(request, "logout.html")
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
