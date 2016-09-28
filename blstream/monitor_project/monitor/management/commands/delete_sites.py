from django.core.management.base import BaseCommand, CommandError
from monitor.models import TrackedSite


class Command(BaseCommand):
    help = 'Delete all tracked sites'

    def handle(self, *args, **options):
        TrackedSite.objects.all().delete()
