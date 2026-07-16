from django.db import models


class WasteReport(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Verified", "Verified"),
        ("Collected", "Collected"),
        ("Recycled", "Recycled"),
    ]

    reporter_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    waste_type = models.CharField(max_length=100)
    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reporter_name} - {self.status}"