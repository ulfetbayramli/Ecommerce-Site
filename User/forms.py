from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth.forms import (UserCreationForm, 
                                    AuthenticationForm, 
                                    UsernameField, 
                                    PasswordChangeForm,
                                    PasswordResetForm,
                                    SetPasswordForm)


from django.contrib.auth import  get_user_model,password_validation
User = get_user_model()


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password'
            }),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email', 
            'password1',
            'password2', 
        )
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),        
        }


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Confirm password is not same with password')
        return password2

    def _post_clean(self):
        super()._post_clean()
        password1 = self.cleaned_data.get('password1')
        # print('here', self.instance.username)
        try:
            password_validation.validate_password(password1, self.instance)
        except forms.ValidationError as error:
            self.add_error('password1', error)
        return password1



# class UserRegisterForm(forms.ModelForm):
#     print("Formlar")

#     password1 = forms.CharField(label="Password")
#     password2 = forms.CharField(label="Confirm Password")
#     email = forms.CharField(label="Email", required=True)
                                                            
#     class Meta:
#         model = get_user_model()
#         fields = ('username', 'password1', 'password2', "email")
        
#         print("Wifget")
        # widgets = {
        #     'first_name': forms.TextInput(attrs={'class': 'input-text',
        #                                         'placeholder': "Your First Name"}),
        #     'last_name': forms.TextInput(attrs={'class': 'input-text',
        #                                         'placeholder': "Your Last Name"}),

        #     # 'email': forms.TextInput(attrs={'class': 'input-text',
        #     #                                     'placeholder': "Your Last Name"}),
        #     'username': forms.TextInput(attrs={'class': 'input-text',
        #                                         'placeholder': "Your Username"}),
        # }

    # def clean_password2(self):
    #     password1 = self.cleaned_data["password1"]
    #     password2 = self.cleaned_data["password2"]

    #     if password1 != password2:
    #         raise forms.ValidationError("Password and confirm password doesn't match")
    #     return password2

class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={
            'class': 'input-text', 
            'placeholder': 'Your Username'
        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'input-text',
            'placeholder': 'Your Password'
        }))
        
class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Email Address", widget=forms.EmailInput(
        attrs={
            'class': 'input-text',
            'placeholder': 'Your Email Address'
        }))
        
class CustomSetPasswordForm(SetPasswordForm):
        new_password1 = forms.CharField(required=True, label='New Password',
            widget=forms.PasswordInput(
                attrs={
                    'class': 'input-text',
                    'placeholder': 'Your New Password'
                }))
        new_password2 = forms.CharField(required=True, label='Confirm New Password',
            widget=forms.PasswordInput(
                attrs={
                    'class': 'input-text',
                    'placeholder': 'Confirm Your New Password'
                }))

class PasswordChangeCustomForm(PasswordChangeForm):
        old_password = forms.CharField(required=True, label='Old Password',
            widget=forms.PasswordInput(
                attrs={
                    'class': 'input-text',
                    'placeholder': 'Your Old Password'
                }))

        new_password1 = forms.CharField(required=True, label='New Password',
            widget=forms.PasswordInput(
                attrs={
                    'class': 'input-text',
                    'placeholder': 'Your New Password'
                }))
        new_password2 = forms.CharField(required=True, label='Confirm New Password',
            widget=forms.PasswordInput(
                attrs={
                    'class': 'input-text',
                    'placeholder': 'Confirm Your New Password'
                }))

class AccountInformationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input-text'}),
            'last_name': forms.TextInput(attrs={'class': 'input-text'}),
            'email': forms.EmailInput(attrs={'class': 'input-text'})
        }
