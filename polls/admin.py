from django.contrib import admin
from .models import *

admin.site.register(WebUser)
admin.site.register(Book)
admin.site.register(Rentlist)

# Register your models here.
