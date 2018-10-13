from django import forms


class AddressbookEntryForm(forms.Form):
    pk = forms.CharField(widget=forms.HiddenInput, required=False)
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    telephone = forms.RegexField(
        regex=r'^\+[0-9]{2}\s[0-9]+\s[0-9]{6,}$',
        max_length=20,
        error_messages={
            'invalid': u'Telephone number specified is not correct. It must be of the form: +XX XXXX XXXXXX'
        },
        label='Telephone number')
