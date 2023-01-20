from django import forms
from .models import ContactUs, Subscriber





class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        exclude = ['user_id']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-text'}),
            'last_name': forms.TextInput(attrs={'class': 'input-text'}),
            'telephone': forms.TextInput(attrs={'class': 'input-text'}),
            'email': forms.EmailInput(attrs={'class': 'input-text'}),
            'comment': forms.Textarea(attrs={'class': 'input-text', 'rows': 5, 'cols': 3})
        }

class SubscriberForm(forms.ModelForm):
    
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'input-text required-entry validate-email',
                                            'type': 'text'})
        }