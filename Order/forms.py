from django import forms
from .models import address_information, billing_addresses, shipping_addresses, order

class AddressInfoForm(forms.ModelForm):
   
    class Meta:
        model = address_information
        exclude = ['user_id']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-text'}),
            'last_name': forms.TextInput(attrs={'class': 'input-text'}),
            'telephone': forms.TextInput(attrs={'class': 'input-text'}),
            'email': forms.EmailInput(attrs={'class': 'input-text'}),
            'street_address': forms.TextInput(attrs={'class': 'input-text'}),
            'country': forms.TextInput(attrs={'class': 'input-text'}),
            'city': forms.TextInput(attrs={'class': 'input-text'}),
            'province': forms.TextInput(attrs={'class': 'input-text'}),
            'zip': forms.TextInput(attrs={'class': 'input-text'}),
            'is_billing': forms.CheckboxInput(attrs={'class': 'checkbox', 'required': False}),
            'is_shipping': forms.CheckboxInput(attrs={'class': 'checkbox', 'required': False}),
        }
        labels = {
            'is_billing': "Use as my default billing address: ",
            'is_shipping': "Use as my default shipping address: ",
        }

class BillingInfoForm(forms.ModelForm):

    class Meta:
        model = billing_addresses
        exclude = ['user_id']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-text'}),
            'last_name': forms.TextInput(attrs={'class': 'input-text'}),
            'telephone': forms.TextInput(attrs={'class': 'input-text'}),
            'email': forms.EmailInput(attrs={'class': 'input-text'}),
            'street_address': forms.TextInput(attrs={'class': 'input-text'}),
            'country': forms.TextInput(attrs={'class': 'input-text'}),
            'city': forms.TextInput(attrs={'class': 'input-text'}),
            'province': forms.TextInput(attrs={'class': 'input-text'}),
            'zip': forms.TextInput(attrs={'class': 'input-text'}),
        }

class ShippingInfoForm(forms.ModelForm):

    class Meta:
        model = shipping_addresses
        exclude = ['user_id']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-text'}),
            'last_name': forms.TextInput(attrs={'class': 'input-text'}),
            'telephone': forms.TextInput(attrs={'class': 'input-text'}),
            'email': forms.EmailInput(attrs={'class': 'input-text'}),
            'street_address': forms.TextInput(attrs={'class': 'input-text'}),
            'country': forms.TextInput(attrs={'class': 'input-text'}),
            'city': forms.TextInput(attrs={'class': 'input-text'}),
            'province': forms.TextInput(attrs={'class': 'input-text'}),
            'zip': forms.TextInput(attrs={'class': 'input-text'}),
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model = order
        fields = ['address']
        widgets = {
            'address': forms.Select(attrs={'class': 'address-select'})
        }