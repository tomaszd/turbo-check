from django.shortcuts import render

from monitor.models import TrackedSite


def index(request):
    """Basic view to see the most recent statuses of tracked sites"""
    newest_status = TrackedSite.objects.get_newest_status()

    return render(request,
                  'monitor/statuses.html',
                  {"newest_status": newest_status}
                  )
