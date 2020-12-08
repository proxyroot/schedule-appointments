from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from schedules.serializers import ScheduleSerializer
from schedules.models import Schedule


@csrf_exempt
@api_view(["GET"])
def list_schedule(request, user_id):
    """
    List all schedules for a given user_id
    """
    snippets = Schedule.objects.filter(user_id=user_id)
    serializer = ScheduleSerializer(snippets, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(["POST"])
def create_schedule(request):
    """
    create schedule if valid and return 201 else throw validation error
    """
    serializer = ScheduleSerializer(data=request.data)

    # Check if the request data is valid
    if not serializer.is_valid():
        return JsonResponse(serializer.errors, status=400)

    # Check if the schedule already exists to return error
    validated_data = serializer.validated_data
    already_exists = Schedule.objects.filter(
        user_id=validated_data["user_id"],
        appointment_date=validated_data["appointment_date"],
    ).exists()

    if already_exists:
        return JsonResponse(
            "Another appointment already exists on same day", status=400, safe=False
        )

    # Persist the data
    serializer.save()
    return JsonResponse(serializer.data, status=201)
