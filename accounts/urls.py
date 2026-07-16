from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path("about/", views.about, name="about"),

    path("waste-information/", views.waste_information, name="waste_information"),

    path("contact/", views.contact, name="contact"),

    path("register/", views.register_page, name="register_page"),

    path("register/save/", views.register, name="register"),

    path("login/", views.login_page, name="login_page"),

    path("login/check/", views.login, name="login"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("logout/", views.logout_view, name="logout"),

]