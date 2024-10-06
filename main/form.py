from django import forms
from .models import Letter, Mail, Client


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = ('name', 'mail_time_start', 'mail_time_finish', 'mail_regularity', 'mail_status', 'clients', 'message')
        widgets = {
            'mail_time_start': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={
                    'type': 'datetime-local',
                }
            ),
            'mail_time_finish': forms.DateTimeInput(
                format='%Y-%m-%dT%H:%M',
                attrs={
                    'type': 'datetime-local',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mail_time_start'].input_formats = ['%Y-%m-%dT%H:%M']
        self.fields['mail_time_finish'].input_formats = ['%Y-%m-%dT%H:%M']


class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ('let_about', 'let_text')


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('email', 'name', 'about')
