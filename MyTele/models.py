from django.db import models


class AddressbookEntry(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return u'{0} {1} ({2})'.format(self.name,
                                       self.surname,
                                       self.telephone)
