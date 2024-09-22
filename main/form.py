from django import forms
from .models import Letter, Mail, Client


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('name', 'mail_time_start', 'mail_time_finish', 'mail_regularity', 'mail_status', 'clients', 'message')


class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ('let_about', 'let_text')


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('email', 'name', 'about')
