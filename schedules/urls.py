from django.urls import path

from . import views

urlpatterns = [
    path("", views.create_schedule, name="create"),
    path("<int:user_id>/", views.list_schedule, name="list"),
]
