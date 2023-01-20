from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from celery import shared_task
# from account.utils.tokens import account_activation_token
from User.utils.tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site



@shared_task
def send_confirmation_mail(user):
    token = account_activation_token.make_token(user) # check does user exist
    uid = urlsafe_base64_encode(force_bytes(user.pk)) #check who is user

    subject = 'Activate Your SuperB Account'
    redirect_url = f"http://localhost:8000{reverse_lazy('confirmation', kwargs={'uidb64': uid,'token': token})}"
    body = render_to_string('email/confirmation_email.html', context={'user': user,'redirect_url': redirect_url,})
    msg = EmailMessage(subject='Email Verification', body=body,
                       from_email=settings.EMAIL_HOST_USER, to=[user.email], )
    msg.content_subtype = 'html'
    msg.send()
