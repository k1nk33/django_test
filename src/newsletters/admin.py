from django.contrib import admin

# Register your models here.
# No need to reference newsletters because we're inside newsletters, just .models
from .models import SignUp


admin.site.register(SignUp)

