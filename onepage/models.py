from django.db import models
from django.core.validators import RegexValidator




class Enquiry(models.Model):

    name = models.CharField(max_length=265)
    email_or_contact = models.CharField(max_length=265,validators=[
        RegexValidator(
            regex=r'^(\d{10}|\w+@\w+\.\w{2,3})$',
            message='Please enter a valid email or contact number.'
        )
    ])
    subject = models.CharField(max_length=265, blank=True)
    message = models.CharField(max_length=265, blank=True)

    def __str__(self):
        return str(f'{str(self.name)}:{str(self.email_or_contact)}')








