from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from User.views import home, home_social, home_courses, home_products, login, demo, marketplace
from User.views import view_product, download_product, test_download, test
from Instructors.views import instructor_home, instructor_profile, create_product, create_course
from Instructors.views import instructor_view_products, instructor_courses, view_edit_course

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home, name="home"),
    url(r'^social/', home_social, name="social"),
    url(r'^products/', home_products, name="products"),
    url(r'^courses/', home_courses, name="courses"),
    url(r'^login/', login, name="login"),
    url(r'^$', demo, name="demo"),

    url(r'^marketplace/', marketplace, name="marketplace"),

    url(r'^view-product/', view_product, name="view_product"),
    url(r'^download-product/', download_product, name="download_product"),

    url(r'^test-download/', test_download, name="test_download"),

    # INSTRUCTOR SIDE
    url(r'^instructor-home/', instructor_home, name="instructor_home"),
    url(r'^instructor-profile/', instructor_profile, name="instructor_profile"),
    url(r'^tinymce/', include('tinymce.urls')),
    # CREATE PRODUCT
    url(r'^add-product/', create_product, name="add_product"),
    url(r'^view-instructor-products/', instructor_view_products, name="instructor_view_products"),
    # CREATE COURSE
    url(r'^create-course/', create_course, name="create_course"),
    url(r'^instructor-courses/', instructor_courses, name="instructor_courses"),
    url(r'^view-course/', view_edit_course, name="view_edit_course"),
    url(r'^test/', test, name="test"),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
