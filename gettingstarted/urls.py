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
    path("import/", hello.views.p_import, name="pw_import"),
    path("add_product/", hello.views.p_add, name="p_add"),
    path("manage_product/", hello.views.p_manage, name="p_manage"),
	path("add_category/", hello.views.c_add, name="c_add"),
	path("manage_category/", hello.views.c_manage, name="c_manage"),
	path("add_warehouse/", hello.views.w_add, name="w_add"),
	path("manage_warehouse/", hello.views.w_manage, name="w_manage"),
	path("export_product/", hello.views.export, name="export"),
	path("invoice/", hello.views.invoice, name="invoice"),
	path("report/", hello.views.report, name="report"),
	path("contact_us/", hello.views.contact_us, name="contact_us"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
