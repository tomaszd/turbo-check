from __future__ import absolute_import

from celery.task import periodic_task
from celery.task import task
from celery.task.schedules import crontab
from celery import shared_task


from monitor.models import TrackedSite
from monitor.models import PeriodicCheck





_interval = PeriodicCheck.objects.get_newest_periodic_check()
if not _interval:
    periodic_check = 10
else:
    periodic_check = str(_interval.interval)


@periodic_task(run_every=crontab(minute='*/{}'.format(periodic_check)))
def get_newest_status():
    """
    Periodically get the newest statuses of tracked sites
    """
    TrackedSite.objects.monitor_sites()


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
