expenses_tracker
================

Simple app to track my expenses. 

Sign in with test/test at http://expenses.msaizar.com 

Deployment
==========

```bash
heroku create
git push heroku master
heroku ps:scale web=1
heroku config:set DJANGO_SETTINGS_MODULE=expenses_tracker.settings.heroku
heroku run python manage.py syncdb
heroku run python manage.py migrate
```
