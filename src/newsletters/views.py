# Import from settings.py for send_mail
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm, ContactForm


# # Create your views here.
def home(request):
    # Display the user initiating the request
    # print "User is %s" % request.user

    # Test if the user has been authenticated already
    # if request.user.is_authenticated():
    # enter dynamic content here

    # Displays the POST data on submit click
    # if request.method == 'POST':
    #     print request.POST

    title = "My Title"
    # If there is Post dat send it through the form, otherwise send none.
    form = SignUpForm(request.POST or None)

    # Context dictionary to pass to the template
    # Context variable ties to template tag in html
    context = {
        "template_title": title,
        "form": form
    }

    # If the form passes all previous validations, including builtins
    if form.is_valid():
        print 'Is Valid'
        # Skips validation to work with data, does not save data
        instance = form.save(commit="False")
        name = form.cleaned_data.get('name')

        # If the name variable is empty, set a default
        if not name:
            name = "Darren Dowdall"
        instance.name = name

        # Displays the associated variables
        # print instance.email
        # print instance.timestamp

        # Using the objects save method?
        # Save details to the db
        instance.save()
        new_title = "Cheers!"

        # Set new dynamically altered context variable (after form completion)
        context = {
            "template_title": new_title,
        }

    # Render combines the different components
    # that make up the final product
    return render(request, "base.html", context)


# Second method for forms
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # # For each Key/Value pair in the cleaned data dict
        # for key in form.cleaned_data:
        #     # Display the corresponding index
        #     print form.cleaned_data.get(key)

        # Or to display the key. value pairs
        # for key, value in form.cleaned_data.iteritems():
        #   print key, value
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        name = form.cleaned_data.get('name')

        # Send email related variables
        subject = 'Test Contact Form'
        contact_msg = "%s : %s via %s" % (
            name,
            message,
            email,
            )

        # from_email = 'someone@somwhere.com'
        # to_email = ['someonelse@somewherelse.com']
        # send_mail(
        #     subject,
        #     contact_msg,
        #     from_email,
        #     to_email,
        #     fail_silently=False,
        #     )

    context = {
        "form": form,
    }

    return render(request, 'forms.html', context)
