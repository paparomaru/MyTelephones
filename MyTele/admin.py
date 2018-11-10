from django.contrib import admin
from MyTele.models import AddressBookEntry
from MyTele.models import Organization


admin.site.register(Organization)
admin.site.register(AddressBookEntry)
