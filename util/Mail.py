from django.core.mail import send_mail
from dotenv import load_dotenv
import os

load_dotenv()

def SendMail(subject, content, recipient_list):
    send_mail(
        subject= subject,
        message=content,
        from_email= os.getenv('EMAIL_HOST_USER'),
        recipient_list=recipient_list,
        fail_silently=False
    )