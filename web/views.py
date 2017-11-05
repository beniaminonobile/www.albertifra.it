# coding: utf-8
from django.http import HttpResponseRedirect

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.views.generic import View


class SendEmailView(View):
    """
    Send email view

    """
    def post(self, request):
        name = None
        email = None
        message = None
        if request.POST.get('name'):
            name = request.POST.get('name')
        if request.POST.get('email'):
            email = request.POST.get('email')
        if request.POST.get('message', False):
            message = request.POST.get('message')
        if name and email and message:
            recipient = settings.EMAIL_RECIPIENT
            mail_message = EmailMessage(u'richiesta info da {} - {}'.format(name, email), message, email, recipient)
            mail_message.send()
            messages.add_message(request, messages.SUCCESS, (u'Email inviata correttamente'))
        else:
            messages.add_message(request, messages.WARNING, (u'Invio email non riuscito'))
        return HttpResponseRedirect('/#footer')
