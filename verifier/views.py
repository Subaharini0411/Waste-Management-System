from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import Verifier
from reports.models import WasteReport


def verifier_login_page(request):
    return render(request, "verifier_login.html")


@csrf_exempt
def verifier_login(request):

    if request.method == "POST":

        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")

        try:
            verifier = Verifier.objects.get(
                username=username,
                password=password
            )

            request.session["verifier_id"] = verifier.id

            return JsonResponse({
                "success": True,
                "message": "Login Successful"
            })

        except Verifier.DoesNotExist:

            return JsonResponse({
                "success": False,
                "message": "Invalid Username or Password"
            })

    return JsonResponse({
        "success": False,
        "message": "Invalid Request"
    })


def verifier_dashboard(request):

    reports = WasteReport.objects.all().order_by("-created_at")

    context = {
        "reports": reports,
        "total_reports": reports.count(),
        "pending": reports.filter(status="Pending").count(),
        "verified": reports.filter(status="Verified").count(),
        "collected": reports.filter(status="Collected").count(),
        "recycled": reports.filter(status="Recycled").count(),
    }

    return render(request, "verifier_dashboard.html", context)


def update_status(request, report_id):

    report = get_object_or_404(WasteReport, id=report_id)

    if report.status == "Pending":
        report.status = "Verified"

    elif report.status == "Verified":
        report.status = "Collected"

    elif report.status == "Collected":
        report.status = "Recycled"

    report.save()

    return redirect("/verifier/dashboard/")