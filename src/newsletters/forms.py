from django import forms
from .models import SignUp


# Second method for forms, instead of using models!
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(required=False)


class SignUpForm(forms.ModelForm):

    # Class for Metadata
    class Meta:
        model = SignUp
        fields = ['name', 'email']

    # Adds to built in email validation tool
    # Syntax of "clean_variable" once defined
    # as a function, overwrites a django function
    # of the same name
    def clean_email(self):
        # "Cleaned_data" is a dictionary of scrubbed
        # data from the forms entry fields
        email = self.cleaned_data.get('email')
        # Displays the dictionary in terminal
        print self.cleaned_data
        user, provider = email.split('@')
        domain, extension = provider.split('.')

        # Specify the match details for the filter
        # Example is a valid college address
        if not extension == "edu":
            # Raise an exception if invalid details are supplied
            raise forms.ValidationError("Please use a valid '.edu' address!")
        return email

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     first, last = name.split(' ')
    #     if first != 'Darren':
    #         raise forms.ValidationError("I can't let you do that %s!" % first)
    #     return name
