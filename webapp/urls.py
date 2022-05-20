from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("services/", views.services, name="services"),
    path("pricing/", views.pricing, name="pricing"),
    path("itsolution/", views.itsolution, name="itsolution"),
    path("about-us/", views.aboutus, name="about-us"),
    path("contact-us/", views.contactus, name="contact-us"),
    path("career/", views.career, name="career"),
    path("support/", views.support, name="support"),
    path("404/", views.notfound, name="404")
]