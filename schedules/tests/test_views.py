import pytest

from django.urls import reverse
from rest_framework import status
from schedules.views import create_schedule, list_schedule
from schedules.tests.factories import ScheduleFactory


@pytest.mark.django_db
def test_create_schedule_happy_path(rf):
    data = {"appointment_date": "2020-11-10", "appointment_time": "10:01", "user_id": 1}
    request = rf.post(reverse("schedules:create"), data, format="json")
    response = create_schedule(request)
    assert response.status_code == status.HTTP_201_CREATED

    # Check that creating the same day again throws 400
    response = create_schedule(request)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert b"Another appointment already exists on same day" in response.content


@pytest.mark.django_db
def test_get_schedule(rf):
    schedule = ScheduleFactory()
    request = rf.get(reverse("schedules:list", args=[schedule.user_id]))
    request.is_internal = True
    response = list_schedule(request, schedule.user_id)
    assert response.status_code == status.HTTP_200_OK
