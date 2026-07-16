from django.urls import path
from . import views

urlpatterns = [

    path('', views.report_page, name='report'),

    path('save/', views.save_report, name='save_report'),

    path("myreports/", views.my_reports, name="my_reports"),

]