from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("stock/", hello.views.stock, name="stock"),
    path("login/", hello.views.login, name="login"),
    path("import_product/", hello.views.p_import, name="p_import"),
    path("add_product/", hello.views.add_product, name="add_product"),
    path("add_pdt_hid/", hello.views.add_pdt_hid, name="add_pdt_hid"),
    path("manage_product/", hello.views.manage_product, name="manage_product"),
	path("add_category/", hello.views.add_category, name="add_category"),
	path("manage_category/", hello.views.manage_category, name="manage_category"),
	path("add_warehouse/", hello.views.add_warehouse, name="add_warehouse"),
	path("manage_warehouse/", hello.views.manage_warehouse, name="manage_warehouse"),
	path("export_product/", hello.views.export, name="export"),
	path("invoice/", hello.views.invoice, name="invoice"),
	path("report/", hello.views.report, name="report"),
	path("contact_us/", hello.views.contact_us, name="contact_us"),
	path("add_war_hid/", hello.views.add_war_hid, name="add_war_hid"),
	path("contact_us/", hello.views.contact_us, name="contact_us"),
	path("contact_us/", hello.views.contact_us, name="contact_us"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
