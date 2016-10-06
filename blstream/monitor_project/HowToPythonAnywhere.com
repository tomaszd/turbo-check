python manage.py collectstatic


http://tomaszd.pythonanywhere.com/monitor/
http://tomaszd.pythonanywhere.com/admin/

changes in settings 


crontab -e 

add here cron.sh

python anywhere is blocking via 403 majority of requests

whitelist is there : 
https://www.pythonanywhere.com/whitelist/

possible sites are there : 
python_anywhere_sites
