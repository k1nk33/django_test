from django.contrib import admin

# Register your models here.

# No need to reference newsletters, relative reference good enough
from .models import SignUp
from .forms import SignUpForm


class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"]
    form = SignUpForm
    # class Meta:
    #     model = SignUp



admin.site.register(SignUp, SignUpAdmin)

