import factory

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save


class Command(BaseCommand):
    help = "Creates test user for E2E testing"

    @factory.django.mute_signals(post_save)
    def handle(self, *args, **options):
        # create test user
        user = get_user_model()(username="admin", email="admin@proxyroot.com")
        user.set_password("admin")
        user.is_superuser = True
        user.is_staff = True
        user.save()
