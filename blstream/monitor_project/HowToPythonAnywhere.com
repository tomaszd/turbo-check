python manage.py collectstatic


http://tomaszd.pythonanywhere.com/monitor/
http://tomaszd.pythonanywhere.com/admin/

changes in settings 


crontab -e 

add here cron.sh
