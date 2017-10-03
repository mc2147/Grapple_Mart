from django.conf.urls import url
from django.contrib import admin
from User.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', Home, name="Home"),
    url(r'^social/', Home_Social, name="Social"),
    url(r'^products/', Home_Products, name="Products"),
    url(r'^courses/', Home_Courses, name="Courses"),
    url(r'^$', Login, name="Login"),

    url(r'^add-product/', Create_Product, name="Add_Products"),

]
