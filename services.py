from datetime import datetime, timedelta

import pytz
from django.core.mail import send_mail
from django.db.models import Max

from config import settings
from config.settings import EMAIL_HOST_USER
from main.models import Mail, MailingLog


def trying_mail(mail, client, current_datetime):
    status_mail = ''
    answer_mail = ''
    try:
        send_mail(subject=mail.name,
                  message=mail.message,
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[client.email, ]
                  )
        status_mail = 'успешно'

    except Exception as e:
        status_mail = 'ошибка'
        answer_mail = str(e)

    MailingLog.objects.create(time=current_datetime,
                              status=status_mail,
                              answer=answer_mail,
                              client=client,
                              mail=mail
                              )


def my_job():
    zone = pytz.timezone(settings.TIME_ZONE)
    today = datetime.now(zone)
    print(zone)
    current_datetime = datetime.now(zone)
    print(current_datetime)
    dataset = Mail.objects.filter(mail_time_start__lte=current_datetime).filter(mail_status__in=('Запущена', 'Создана'))

    for mail in dataset:
        if mail.mail_time_finish < current_datetime:
            mail.mail_status = 'Завершена'
        else:
            if mail.mail_status == 'Создана' and mail.mail_time_start <= current_datetime:
                mail.mail_status = 'Запущена'
            if today >= mail.next_time_mailing:
                for client in mail.clients.all():
                    trying_mail(mail, client, current_datetime)
                if mail.mail_regularity == 'Ежедневно':
                    mail.next_time_mailing += timedelta(days=1)
                elif mail.mail_regularity == 'Еженедельно':
                    mail.next_time_mailing += timedelta(days=7)
                elif mail.mail_regularity == 'Ежемесечно':
                    mail.next_time_mailing += timedelta(month=1)
        mail.save()












