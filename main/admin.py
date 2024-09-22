from django.contrib import admin
from .models import Client, Mail, MailingLog, Letter


class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'about')
    search_fields = ('email', 'name')
    list_filter = ('about',)


class LetterAdmin(admin.ModelAdmin):
    list_display = ('let_about',)
    search_fields = ('let_about',)


class MailAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail_status', 'mail_time_start', 'mail_regularity', 'message')
    list_filter = ('mail_status', 'mail_regularity')
    search_fields = ('mail_status', 'message')


class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('time', 'status')
    list_filter = ('status',)
    search_fields = ('status',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Letter, LetterAdmin)
admin.site.register(Mail, MailAdmin)
admin.site.register(MailingLog, MailingLogAdmin)