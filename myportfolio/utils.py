from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def send_email(email, title, context, email_html_message, email_plaintext_message):
    email_html_message = render_to_string(email_html_message, context)
    email_plaintext_message = render_to_string(email_plaintext_message, context)
    
    msg = EmailMultiAlternatives(
        # title:
        title,
        # message:
        email_plaintext_message,
        # from:
        settings.DEFAULT_FROM_EMAIL,
        # to:
        [email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()