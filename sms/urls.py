from django.conf.urls import url
from . import views

app_name = 'sms'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<message_sid>\w+)', views.detail, name='detail'),
    url(r'^delete/(?P<message_sid>\w+)', views.delete_sms, name='delete'),
]