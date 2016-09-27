import datetime
from django.db import models
import requests
import time
from twisted.spread.pb import respond

# Create your models here.
class TrackedSite(models.Model):
    name = models.CharField(max_length=128, unique=True)
    content_requirement = models.CharField(max_length=128, default="")

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
            site_status = "down"
            total_time = 0
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
    def __unicode__(self):
        return "<" + str(self.site) + "_" + str(self.site_status) + \
               "_" + str(self.timestamp) + ">"

