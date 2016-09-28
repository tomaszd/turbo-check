import datetime
import requests
import time

from django.db import models
from model_utils.models import TimeStampedModel


class TrackedSiteManager(models.Manager):

    def monitor_sites(self):
        for site in self.all():
            site.create_status()


# Create your models here.
class TrackedSite(models.Model):
    name = models.CharField(max_length=128, unique=True)
    content_requirement = models.CharField(max_length=128, default="")

    objects = TrackedSiteManager()

    def __unicode__(self):
        return self.name

    def create_status(self):
        """
        SiteStatus.objects.create(
          content_validated=True,
          site_status="OK",
          timestamp=datetime.datetime.now(),
          site=TrackedSite.objects.all()[0])
        """
        _content_validated = False
        _site_status, _total_time, _response = self._check_status()
        if _response:
            _content_validated = self._validate_content(_response)

        new_status = SiteStatus.objects.create(
            content_validated=_content_validated,
            site_status=_site_status,
            timestamp=datetime.datetime.now(),
            time=_total_time,
            site=self)
        return new_status

    def _check_status(self):
        response = None
        try:
            start = time.time()
            response = requests.get(self.name)
            total_time = time.time() - start
            site_status = response.status_code
        except:
            total_time = 0
            site_status = "down"
        return site_status, total_time, response

    def _validate_content(self, response):
        if self.content_requirement in response.text:
            return True
        return False


class SiteStatus(models.Model):
    site_status = models.CharField(max_length=128)
    content_validated = models.BooleanField(default=False)
    timestamp = models.DateTimeField()
    site = models.ForeignKey(TrackedSite)
    time = models.FloatField()
    location = models.CharField(max_length=128, default="Poland")

    def __unicode__(self):
        return "<" + str(self.site) + "_" + str(self.site_status) + \
               "_" + str(self.timestamp) + ">"


class PeriodicCheckManager(models.Manager):

    def get_newest_periodic_check(self):
        if len(self) == 0:
            return
        return self.order_by("-created")[0]


class PeriodicCheck(TimeStampedModel):

    """Class needed for storing the amount of time between periodic checks"""
    # amounts of minutes between periodic checks
    interval = models.IntegerField(default=10)
    # common name for interval
    name = models.CharField(max_length=128, default="daily_check")

    objects = PeriodicCheckManager()

    def __unicode__(self):
        return "<" + self.name + ": " + str(self.interval) + ">"
