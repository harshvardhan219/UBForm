from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'age', 'email', 'mobile_number', 'pincode', 'highest_qualification', 'university', 'status')

    widget = {
        'first_name': forms.TextInput(attrs={'class' : 'form-control'})
    }