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
    path("about/", hello.views.about, name="about"),
    path("notification/", hello.views.notification, name="notification"),
    path("contact/", hello.views.contact, name="contact"),
	path("add_product/", hello.views.add_product, name="add_product"),
	path("insproduct/", hello.views.insproduct, name="insproduct"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
