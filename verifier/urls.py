from django.urls import path
from . import views

urlpatterns = [

    path(
        "login/",
        views.verifier_login_page,
        name="verifier_login"
    ),

    path(
        "login/check/",
        views.verifier_login,
        name="verifier_login_check"
    ),

    path(
        "dashboard/",
        views.verifier_dashboard,
        name="verifier_dashboard"
    ),

    path(
        "update/<int:report_id>/",
        views.update_status,
        name="update_status"
    ),

]