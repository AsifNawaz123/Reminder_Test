from __future__ import absolute_import
from celery import Celery
import os
from django.conf import settings

#Set Django settings module for celery.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'appointments.settings.production')
app = Celery('appointments')
mapp.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
