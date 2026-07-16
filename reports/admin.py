from django.contrib import admin
from .models import WasteReport

@admin.register(WasteReport)
class WasteReportAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "reporter_name",
        "location",
        "waste_type",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "waste_type",
    )

    search_fields = (
        "reporter_name",
        "location",
        "waste_type",
    )