from django.contrib import admin

from monitor.models import SiteStatus
from monitor.models import TrackedSite
from monitor.models import PeriodicCheck


admin.site.register(TrackedSite)
admin.site.register(SiteStatus)
admin.site.register(PeriodicCheck)
