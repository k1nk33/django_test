from django import forms
from .models import SignUp


class SignUpForm(forms.ModelForm):

    class Meta:
        models = SignUp
        fields = ['name', 'email']

    # Adds to built in email validation tool
    def clean_email(self):
        email = self.cleaned_data.get('email')
        user, provider = email.split('@')
        domain, extension = provider.split('.')

        # Specify the filter
        if not extension == "edu":
            raise forms.ValidationError("Please use a valid '.edu' address!")
        return email

    def clean_name(self):
        name = self.cleaned_data.get('name')
        first, last = name.split(' ')
        if first != 'Darren':
            raise forms.ValidationError("I can't let you do that %s!" % first)
        return name
