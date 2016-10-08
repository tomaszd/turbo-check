# this is a cron file.
# please add it to your personal cron to monitor pages
# at the frequency you really
cd /home/tomaszd/Turbo-Check/blstream/monitor_project
source /home/tomaszd/.virtualenvs/blstream/bin/activate
python manage.py syncdb
python manage.py monitor_sites
