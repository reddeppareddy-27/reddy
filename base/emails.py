from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
import logging

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
import logging

# Logger for error handling
logger = logging.getLogger(__name__)

def send_account_activation_email(email, email_token):
    try:
        # Construct the activation link
        activation_link = f'http://127.0.0.1:8000/accounts/activate/{email_token}'

        # Email subject and sender
        subject = 'Activate Your Account'
        email_from = settings.EMAIL_HOST_USER

        # Context for the email template
        context = {
            'activation_link': activation_link
        }

        # HTML and plain-text email content
        html_content = render_to_string('emails/activation.html', context)  # HTML email template
        plain_content = f"Hi, please click the following link to activate your account: {activation_link}"  # Plain text fallback

        # Prepare the email
        email_msg = EmailMultiAlternatives(
            subject=subject,
            body=plain_content,  # Text fallback
            from_email=email_from,
            to=[email],
        )
        email_msg.attach_alternative(html_content, "text/html")  # Attach HTML content

        # Send the email
        email_msg.send()
    except Exception as e:
        logger.error(f"Error sending account activation email: {e}")
        raise

logger = logging.getLogger(__name__)

def send_password_reset_email(email, token):
    try:
        # Construct the reset URL
        reset_url = f'http://127.0.0.1:8000/accounts/reset-password/{token}'
        
        # Email subject and sender
        subject = 'Reset Your Password'
        email_from = settings.EMAIL_HOST_USER

        # Context for the email template
        context = {
            'reset_url': reset_url
        }

        # HTML and plain-text email content
        html_content = render_to_string('emails/reset_password_email.html', context)  # HTML email template
        plain_content = f"Hi, please click the following link to reset your password: {reset_url}"  # Plain text fallback

        # Prepare the email
        email_msg = EmailMultiAlternatives(
            subject=subject,
            body=plain_content,  # Text fallback
            from_email=email_from,
            to=[email],
        )
        email_msg.attach_alternative(html_content, "text/html")  # Attach HTML content

        # Send the email
        email_msg.send()
    except Exception as e:
        logger.error(f"Error sending password reset email: {e}")
        raise