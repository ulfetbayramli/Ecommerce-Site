from django.urls import path
from .views import error, about_us, ContactUs, FAQ, HomePage, searchview
from . import views

urlpatterns = [
    path('404error/', error, name = "error"),
    path('about_us/', about_us, name = "about_us"),
    path('contact_us/', ContactUs.as_view(), name = "contact_us"),
    path('faq/', FAQ.as_view(), name = "faq"),
    path('', HomePage.as_view(), name = "index"),
    path('searchview', views.searchview, name = "searchview")
]