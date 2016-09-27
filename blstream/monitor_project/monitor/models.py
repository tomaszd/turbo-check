from django.db import models

# Create your models here.

class TrackedSite(models.Model):
    name = models.CharField(max_length=128, unique=True)
    content_requirement = models.CharField(max_length=128, default="")

    def __unicode__(self):
        return self.name


class SiteStatus(models.Model):
    site_status = models.CharField(max_length=128, unique=True)
    content_validated = models.BooleanField(default=False)
    timestamp = models.DateTimeField()
    site = models.ForeignKey(TrackedSite)

    def __unicode__(self):
        return self.site, self.site_status, self.timestamp






