from django.urls import path
from . import views

urlpatterns = [

    path("", views.feedback_page, name="feedback"),

    path("save/", views.save_feedback, name="save_feedback"),

]