from django.urls import path
from django.views.decorators.cache import cache_page

from .views import ClientCreateView, ClientDeleteView, ClientUpdateView, ClientsListView, MailsListView, \
    MailCreateView, MailDeleteView, MailUpdateView, LetterCreateView, LetterDeleteView, LetterUpdateView, \
    MailDetailView, ClientDetailView, LetterListView, LetterDetailView, MainPageListView

app_name = 'main'

urlpatterns = [
    path('', cache_page(60)(MainPageListView.as_view()), name='main_page'),
    path('mails_list/', MailsListView.as_view(), name='mails_list'),
    path('clients_list/', ClientsListView.as_view(), name='clients_list'),
    path('mail_detail/<int:pk>', MailDetailView.as_view(), name='mail_detail'),
    path('mail_create/', MailCreateView.as_view(), name='mail_create'),
    path('mail_update/<int:pk>', MailUpdateView.as_view(), name='mail_update'),
    path('mail_delete/<int:pk>', MailDeleteView.as_view(), name='mail_delete'),
    path('client_detail/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('client_delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
    path('letters_list/', LetterListView.as_view(), name='letters_list'),
    path('letter_detail/<int:pk>', LetterDetailView.as_view(), name='letter_detail'),
    path('letter_create/', LetterCreateView.as_view(), name='letter_create'),
    path('letter_update/<int:pk>', LetterUpdateView.as_view(), name='letter_update'),
    path('letter_delete/<int:pk>', LetterDeleteView.as_view(), name='letter_delete'),
]