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

    # If the form passes all previous validations
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
        instance.save()
        new_title = "Cheers!"

        # Set new dynamically altered context variable
        context = {
            "template_title": new_title,
        }

    # Render combines the different components
    # that make up the final product
    return render(request, "home.html", context)


# Second method for forms
def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        "form": form,
    }

    return render(request, 'forms.html', context)
