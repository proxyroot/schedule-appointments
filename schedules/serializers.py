from rest_framework import serializers
from schedules.models import Schedule


class ScheduleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    appointment_time = serializers.TimeField()
    appointment_date = serializers.DateField()

    def create(self, validated_data):
        return Schedule.objects.create(**validated_data)
