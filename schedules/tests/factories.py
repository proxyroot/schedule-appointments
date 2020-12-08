import factory

from schedules.models import Schedule


class ScheduleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Schedule

    user_id = factory.Sequence(lambda n: n)
    appointment_date = factory.Faker("date_object")
    appointment_time = factory.Faker("time_object")
