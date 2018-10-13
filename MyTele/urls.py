from django.urls import re_path
from MyTele.views import index, detail, search, edit

urlpatterns = [
    re_path(r'^edit/(?P<entry_id>\d+)/$', edit, name='edit_existing'),
    re_path(r'^detail/(?P<entry_id>\d+)/$', detail, name='detail'),
    re_path(r'^search/$', search, name='search'),
    re_path(r'^edit/$', edit, name='edit'),
    re_path('', index, 'index', name='index'),
]
