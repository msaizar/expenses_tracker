expenses_tracker
================

Simple app to track my expenses


Deployed Heroku App at http://expenses.msaizar.com
Sign in with test/test

Deployment
==========

heroku create
git push heroku master
heroku ps:scale web=1
heroku config:set DJANGO_SETTINGS_MODULE=expenses_tracker.settings.heroku
heroku run python manage.py syncdb
heroku run python manage.py migrate
