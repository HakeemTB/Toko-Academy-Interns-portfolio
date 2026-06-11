from celery import shared_task
from django.core.mail import send_mail
from .models import ContactMessage

@shared_task(key='ip',)
def send_contact_email_notification(message_id):
    message = ContactMessage.objects.get(id=message_id)
    send_mail(
        subject='New Contact Message',
        message=f'From: {message.email}\n\n{message.message}',
        from_email=message.email,
        recipient_list=['hakeemtony02@gmail.com']
    )