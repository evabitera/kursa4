from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='почта', unique=True)
    name = models.CharField(max_length=100, verbose_name='ФИО')
    about = models.TextField(verbose_name='комментарий')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='юзер')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class Mail(models.Model):
    name = models.CharField(max_length=25, verbose_name='имя рассылки')
    mail_time_start = models.DateTimeField(verbose_name='время рассылки начало', **NULLABLE)
    mail_time_finish = models.DateTimeField(verbose_name='время рассылки конец', **NULLABLE)
    mail_regularity = models.CharField(max_length=40, verbose_name='регулярность',
                                       choices=(('Ежедневно', 'Ежедневно'),
                                                ('Еженедельно', 'Еженедельно'),
                                                ('Ежемесячно', 'Ежемесячно')))
    mail_status = models.CharField(max_length=40, verbose_name='статус расслыки',
                                   choices=(('Создана', 'Создана'),
                                            ('Запущена', 'Запущена'),
                                            ('Завершена', 'Завершена')))
    clients = models.ManyToManyField(Client, blank=True, related_name='clients', verbose_name='клиенты')
    message = models.OneToOneField('Letter', on_delete=models.SET_NULL, **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    next_time_mailing = models.DateTimeField(verbose_name='следующее время расслыки', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mail"
        verbose_name_plural = "Mails"


class Letter(models.Model):
    let_about = models.CharField(max_length=100, verbose_name='тема рассылки')
    let_text = models.TextField(verbose_name='текс рассылки')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='юзер')

    def __str__(self):
        return self.let_about

    class Meta:
        verbose_name = "Letter"
        verbose_name_plural = "Letters"


class MailingLog(models.Model):
    STATUS_SUCCESS = 'success'
    STATUS_ERROR = 'error'

    STATUSES = (
        (STATUS_SUCCESS, 'успешно'),
        (STATUS_ERROR, 'ошибка'),
    )
    time = models.DateTimeField(auto_now_add=True, verbose_name='время последней попыткм рассылки')
    status = models.CharField(max_length=20, choices=STATUSES, verbose_name='статус последней попытки расслыки')
    answer = models.CharField(max_length=250, verbose_name='ответ сервера', **NULLABLE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиенты')
    mail = models.ForeignKey(Mail, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = "MailingLog"
        verbose_name_plural = "MailingLogs"




