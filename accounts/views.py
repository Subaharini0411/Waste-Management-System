from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Reporter
from reports.models import WasteReport
import json


# ---------------- HOME ----------------

def home(request):
    return render(request, "home.html")


# ---------------- ABOUT ----------------

def about(request):
    return render(request, "about.html")


# ---------------- WASTE INFORMATION ----------------

def waste_information(request):
    return render(request, "waste_information.html")


# ---------------- CONTACT ----------------

def contact(request):
    return render(request, "contact.html")


# ---------------- REGISTER ----------------

def register_page(request):
    return render(request, "register.html")


@csrf_exempt
def register(request):

    if request.method == "POST":

        try:
            data = json.loads(request.body)

            fullname = data.get("fullname")
            email = data.get("email")
            phone = data.get("phone")
            address = data.get("address")
            password = data.get("password")

            # Check if email already exists
            if Reporter.objects.filter(email=email).exists():

                return JsonResponse({
                    "success": False,
                    "message": "Email already registered. Please login."
                })

            # Create Reporter
            reporter = Reporter.objects.create(
                full_name=fullname,
                email=email,
                contact=phone,
                address=address,
                password=password
            )

            # Save session
            request.session["reporter_id"] = reporter.id
            request.session["reporter_name"] = reporter.full_name

            return JsonResponse({
                "success": True,
                "message": "Registration Successful",
                "redirect": "/report/"
            })

        except Exception as e:

            return JsonResponse({
                "success": False,
                "message": str(e)
            })

    return JsonResponse({
        "success": False,
        "message": "Invalid Request"
    })


# ---------------- LOGIN ----------------

def login_page(request):
    return render(request, "login.html")


@csrf_exempt
def login(request):

    if request.method == "POST":

        data = json.loads(request.body)

        email = data.get("email")
        password = data.get("password")

        try:

            reporter = Reporter.objects.get(
                email=email,
                password=password
            )

            request.session["reporter_id"] = reporter.id
            request.session["reporter_name"] = reporter.full_name

            return JsonResponse({
                "success": True,
                "message": "Login Successful",
                "redirect": "/report/"
            })

        except Reporter.DoesNotExist:

            return JsonResponse({
                "success": False,
                "message": "Invalid Email or Password"
            })

    return JsonResponse({
        "success": False,
        "message": "Invalid Request"
    })


# ---------------- DASHBOARD ----------------

def dashboard(request):

    total_reports = WasteReport.objects.count()

    pending = WasteReport.objects.filter(status="Pending").count()

    verified = WasteReport.objects.filter(status="Verified").count()

    collected = WasteReport.objects.filter(status="Collected").count()

    recycled = WasteReport.objects.filter(status="Recycled").count()

    return render(request, "dashboard.html", {

        "total_reports": total_reports,
        "pending": pending,
        "verified": verified,
        "collected": collected,
        "recycled": recycled,

    })


# ---------------- LOGOUT ----------------

def logout_view(request):

    request.session.flush()

    return redirect("/")