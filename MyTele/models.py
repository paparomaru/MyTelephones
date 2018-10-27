from django.db import models


class AddressBookEntry(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, default='example@mail.ru')
    komment = models.TextField(default='Komment')

    def __str__(self):
        return u'{0} {1} ({2}) {3}'.format(self.name,
                                           self.surname,
                                           self.telephone,
                                           self.email)
