from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import WasteReport
import json


# ---------------- REPORT PAGE ----------------

def report_page(request):

    reporter_name = request.session.get("reporter_name", "")

    return render(request, "report.html", {
        "reporter_name": reporter_name
    })


# ---------------- SAVE REPORT ----------------

@csrf_exempt
def save_report(request):

    if request.method == "POST":

        data = json.loads(request.body)

        reporter_name = request.session.get("reporter_name")

        if not reporter_name:

            return JsonResponse({
                "success": False,
                "message": "Please login first."
            })

        WasteReport.objects.create(

            reporter_name=reporter_name,

            location=data.get("location"),

            waste_type=data.get("waste_type"),

            description=data.get("description")

        )

        return JsonResponse({

            "success": True,

            "message": "Waste Report Submitted Successfully"

        })

    return JsonResponse({

        "success": False,

        "message": "Invalid Request"

    })


# ---------------- MY REPORTS ----------------

def my_reports(request):

    reporter_name = request.session.get("reporter_name")

    reports = WasteReport.objects.filter(

        reporter_name=reporter_name

    ).order_by("-created_at")

    return render(request, "my_reports.html", {

        "reports": reports,

        "reporter_name": reporter_name

    })