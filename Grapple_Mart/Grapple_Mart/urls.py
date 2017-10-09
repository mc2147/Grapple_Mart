from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from User.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^generic-home/', Generic_Home, name="Generic_Home"),
    url(r'^home/', Home, name="Home"),
    url(r'^social/', Home_Social, name="Social"),
    url(r'^products/', Home_Products, name="Products"),
    url(r'^courses/', Home_Courses, name="Courses"),
    url(r'^$', Login, name="Login"),

    url(r'^marketplace/', Marketplace, name="Courses"),

    url(r'^add-product/', Create_Product, name="Add_Product"),
    url(r'^view-product/', View_Product, name="View_Product"),
    url(r'^download-product/', Download_Product, name="Download_Product"),

    url(r'^test-download/', Test_Download, name="Test_Download"),

    url(r'^instructor-profile-preview/', Instructor_Profile_Preview, name="Instructor_Profile_Preview"),
    url(r'^instructor-profile/', Instructor_Profile, name="Instructor_Profile"),
    url(r'^instructor-bookings/', Instructor_Bookings, name="Instructor_Profile"),
    # url(r'^tinymce/', include('tinymce.urls')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
