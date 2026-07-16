from django.shortcuts import render
from django.http import JsonResponse
from .models import Feedback
from django.views.decorators.csrf import csrf_exempt
import json


def feedback_page(request):
    return render(request, "feedback.html")


@csrf_exempt
def save_feedback(request):

    if request.method == "POST":

        data = json.loads(request.body)

        Feedback.objects.create(
            reporter_name=data.get("reporter_name"),
            email=data.get("email"),
            message=data.get("message")
        )

        return JsonResponse({
            "success": True,
            "message": "Feedback Submitted Successfully"
        })

    return JsonResponse({
        "success": False,
        "message": "Invalid Request"
    })