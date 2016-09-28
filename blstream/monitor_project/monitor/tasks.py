from celery.task import periodic_task
from celery.task import task
from celery.task.schedules import crontab

from monitor.models import TrackedSite
from monitor.models import PeriodicCheck

periodic_check = str(PeriodicCheck.objects.all()[0].interval)


@periodic_task(run_every=crontab(minute='*/{}'.format(periodic_check)))
def get_newest_status():
    """
    Periodically get the newest statuses of tracked sites
    """
    TrackedSite.objects.monitor_sites()
