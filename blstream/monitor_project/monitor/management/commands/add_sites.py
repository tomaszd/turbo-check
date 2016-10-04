from django.core.management.base import BaseCommand, CommandError
from monitor.models import TrackedSite
from optparse import make_option
import os


class Command(BaseCommand):

    help = """Adds new sites from configuration file.
    The format of data should be : \n
    url criteria
    url2 criteria2
    ...
    url5 criteria5"""

    option_list = BaseCommand.option_list + (
        make_option('--file',
                    action='store',
                    dest='file',
                    default=False,
                    help='Custom path to configuration file'),
    )

    def open_file(self, filename):
        # Open a file
        self.stdout.write("Opening file {}".format(filename))
        if not os.path.exists(filename):
            self.stdout.write("Filename {} does not exist".format(filename))
            return

        fo = open(filename, "r+")
        self.stdout.write("Name of the file: {}".format(filename))
        lines = fo.readlines()
        fo.close()

        for line in lines:
            if ('www' in line or 'http' in line) and ' ' in line:
                self.stdout.write("{}URL is OK to track".format(line))
                pass
            else:
                import pdb
                pdb.set_trace()
                self.stdout.write("{} is not a proper "
                                  "line with site url".format(line))
                continue

            site_name, content_requirement = line.split(" ")
            self.stdout.write("site_name : {},"
                              "criteria : {}".format(site_name,
                                                     content_requirement))
            sites = TrackedSite.objects.get_or_create(
                name=site_name,
                content_requirement=content_requirement)

    def handle(self, *args, **options):
        if options['file']:
            self.open_file(options['file'])
        else:
            default_file = 'sites.txt'
            self.stdout.write("Opening default configuration file {}".format(
                              default_file))
            self.open_file('sites.txt')
