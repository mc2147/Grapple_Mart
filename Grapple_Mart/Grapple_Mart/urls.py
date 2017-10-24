from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from User.views import Home, Home_Social, Home_Courses, Home_Products, Login, Demo, Marketplace
from User.views import View_Product, Download_Product, Test_Download, Test
from Instructors.views import Instructor_Home, Instructor_Profile, Create_Product, Create_Course
from Instructors.views import Instructor_View_Products, Instructor_Courses, View_Edit_Course

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', Home, name="Home"),
    url(r'^social/', Home_Social, name="Social"),
    url(r'^products/', Home_Products, name="Products"),
    url(r'^courses/', Home_Courses, name="Courses"),
    url(r'^login/', Login, name="Login"),
    url(r'^$', Demo, name="Demo"),

    url(r'^marketplace/', Marketplace, name="Courses"),

    url(r'^view-product/', View_Product, name="View_Product"),
    url(r'^download-product/', Download_Product, name="Download_Product"),

    url(r'^test-download/', Test_Download, name="Test_Download"),

    # INSTRUCTOR SIDE
    url(r'^instructor-home/', Instructor_Home, name="Instructor_Home"),
    url(r'^instructor-profile/', Instructor_Profile, name="Instructor_Profile"),
    url(r'^tinymce/', include('tinymce.urls')),
    # CREATE PRODUCT
    url(r'^add-product/', Create_Product, name="Add_Product"),
    url(r'^view-instructor-products/', Instructor_View_Products, name="Instructor_View_Products"),
    # CREATE COURSE
    url(r'^create-course/', Create_Course, name="Create_Course"),
    url(r'^instructor-courses/', Instructor_Courses, name="Instructor_Courses"),
    url(r'^view-course/', View_Edit_Course, name="Create_Course"),
    url(r'^test/', Test, name="Create_Course"),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
