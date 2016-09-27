from django.core.management.base import BaseCommand, CommandError
from monitor.models import TrackedSite


class Command(BaseCommand):
    help = 'Checks the statuses for all the Tracked Sites'

    def handle(self, *args, **options):
        TrackedSite.objects.monitor_sites()
