from django.core.management.base import BaseCommand, CommandError
from monitor.models import PeriodicCheck
from optparse import make_option


class Command(BaseCommand):

    help = """Command line to set interval between checks of sites.
    To set interval please use :
    python manage.py set_interval --interval <INT>"""

    option_list = BaseCommand.option_list + (
        make_option('--interval',
                    action='store',
                    dest='interval',
                    default=False,
                    help='amount of minutes for periodic checks of sites'),
    )

    def handle(self, *args, **options):
        if options['interval']:
            try:
                int(options['interval'])
            except ValueError:
                self.stdout.write("{} is not an <int> . Please set <int> as "
                                  "interval value".format(options['interval']))
                return
            interval, created = PeriodicCheck.objects.get_or_create(
                interval=int(options['interval']),
                name="manually added")
            if created:
                self.stdout.write(
                    "New interval created and set: {}".format(interval))
            else:
                self.stdout.write("Interval set: {}".format(interval))

        else:
            PeriodicCheck.objects.get_or_create(
                interval=10,
                name="added Default one by c-line")

            self.stdout.write("No Interval selected! Selecting default 10")
