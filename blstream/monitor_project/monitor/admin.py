from django.contrib import admin

from monitor.models import SiteStatus
from monitor.models import TrackedSite


admin.site.register(TrackedSite)
admin.site.register(SiteStatus)
