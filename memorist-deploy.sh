kill 14107
cd bounswe2018group4/
git pull
git checkout develop

source /home/ubuntu/venv/bin/activate
cd MemoristAPI/
cp -r * /home/ubuntu/memorist.com/
cd /home/ubuntu/memorist.com
pip install -r requirements.txt
python manage.py migrate --settings=MemoristAPI.settings.prod

gunicorn --env DJANGO_SETTINGS_MODULE=MemoristAPI.settings.prod MemoristAPI.wsgi -b :8000 &>> /home/ubuntu/logs/memorist.log &

sed -i "1s/^.*$/kill $!/" /home/ubuntu/memorist-deploy.sh