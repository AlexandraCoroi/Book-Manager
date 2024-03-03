from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import get_object_or_404, render, redirect, reverse, HttpResponse
from django.template.loader import get_template
from django.contrib import messages
from django.utils import timezone
from users.models import Activation
from users.utils.constants import ACTIVATION_AVAILABILITY

def activate_user(request, token):
    activation = get_object_or_404(Activation, token=token)
    if not activation.used and activation.created_at + timezone.timedelta(days=1) > timezone.now():
        user = activation.user
        user.is_active = True
        user.save()

        activation.used = True
        activation.save()



def reset_token_view(request, token):
    pass

def send_activation_email(user):
    domain = Site.objects.get_current().domain
    url = reverse('users:activation:activate', args=(user.activation.token,))
    activation_url = f'{domain}{url}'
    print('activation_url', activation_url)

    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'activation_url': activation_url,
        'availability': ACTIVATION_AVAILABILITY
    }

    template = get_template('emails/activation.html')
    content = template.render(context)
    mail = EmailMultiAlternatives(
        subject='Your account has been created',
        body=content,
        to=[user.email]
    )
    mail.content_subtype = 'html'
    mail.send()