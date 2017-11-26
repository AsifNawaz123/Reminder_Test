from __future__ import absolute_import
from celery import shared_task
from django.conf import settings
from twilio.rest import Client
import arrow
from .models import Appointment

client = Client()

@shared_task
def send_sms_reminder(appointment_id):
    """Send a reminder to a phone"""
    # Get our appointment from the database
    try:
        appointment = Appointment.objects.get(pk=appointment_id)
    except Appointment.DoesNotExist:
        return

    appointment_time = arrow.get(appointment.time, appointment.time_zone.zone)
    body = 'Hi, You have an appointment at {1}'.format(
        appointment.name,
        appointment_time.format('h:mm a')
    )

    message = client.messages.create(
        body=body,
        to=appointment.phone_number,
        from_=settings.TWILIO_NUMBER,
    )
