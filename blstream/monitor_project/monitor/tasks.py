from celery.task import periodic_task
from celery.task import task
from celery.task.schedules import crontab

from monitor.models import TrackedSite


@periodic_task(run_every=crontab(minute='10', hour='1,5,12,18'))
def get_newest_status():
    """
    Periodically get the newest statuses of tracked sites
    """
    TrackedSite.objects.monitor_sites()
