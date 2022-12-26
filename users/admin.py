from django.contrib import admin
from .models import IndividualAccount, CorporateAccount

# Register your models here.
admin.site.register(IndividualAccount)
admin.site.register( CorporateAccount)

