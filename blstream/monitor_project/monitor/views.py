from django.shortcuts import render

from monitor.models import TrackedSite


# note this is a nice place to cache the results of index view
# There is no need to make TrackedSite.objects.get_newest_status()
# more often that periodic check interval.

def index(request):
    """Basic view to see the most recent statuses of tracked sites"""
    newest_status = TrackedSite.objects.get_newest_status()

    return render(request,
                  'monitor/statuses.html',
                  {"newest_status": newest_status}
                  )
