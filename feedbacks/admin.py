from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "reporter_name",
        "email",
        "created_at",
    )

    search_fields = (
        "reporter_name",
        "email",
    )