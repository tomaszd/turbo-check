from django.core.management.base import BaseCommand, CommandError
from monitor.models import SiteStatus


class Command(BaseCommand):
    help = 'Delete all tracked sites'

    def handle(self, *args, **options):
        SiteStatus.objects.all().delete()
