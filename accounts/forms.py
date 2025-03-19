from django import forms

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label="Enter your email", max_length=254)

class SetNewPasswordForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput, label="New Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
