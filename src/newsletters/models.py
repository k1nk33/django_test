from django.db import models

# Create your models here.


class SignUp(models.Model):

    email = models.EmailField()
    # Blank infers a required field
    name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # DB expects a string hence calling the function
    # Return value can be something else once wrapped in python str() function!
    def __unicode__(self):  # python3 __str__ instead
        return self.email
