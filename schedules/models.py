from django.db import models


class Schedule(models.Model):
    user_id = models.IntegerField()
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]
