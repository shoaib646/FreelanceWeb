from django import forms
from .models import Enquiry


CHOICES = [
            ('How accurate does Predicted look to you?', 'How accurate does Predicted look to you?'),
            ('Probably Right', 'Probably Right'),
            ('High', 'High'),
            ('Low', 'Low'),
        ]

class enquiryform(forms.ModelForm):

    class Meta:

        model = Enquiry
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"placeholder":"Name","class":"form-control"}),
            "email_or_contact": forms.TextInput(attrs={ "placeholder":"Email or Contact Number","class":"form-control"}),
            "subject": forms.TextInput(attrs={"placeholder":"Subject","class":"form-control"}),
            "message" : forms.Textarea(attrs={"placeholder":"Message", "class":"form-control"}),
        }






