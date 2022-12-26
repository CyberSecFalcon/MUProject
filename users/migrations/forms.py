# In the forms.py file within your app (users/forms.py), create forms for the signup and profile update processes:

from django import forms
from .models import IndividualAccount, CorporateAccount

class IndividualSignupForm(forms.ModelForm):
    # Form fields for the individual signup process
    class Meta:
        model = IndividualAccount
        fields = ['username', 'password', 'email']

class CorporateSignupForm(forms.ModelForm):
    # Form fields for the corporate signup process
    class Meta:
        model = CorporateAccount
        fields = ['username', 'password', 'email']

class ProfileUpdateForm(forms.ModelForm):
    # Form fields for updating individual and corporate profiles
    class Meta:
        model = IndividualAccount
        fields = ['username', 'email']
    class Meta:
        model = CorporateAccount
        fields = ['username', 'email']
