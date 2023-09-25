from django.contrib import admin
from .models import income, transac, usrs

admin.site.register(usrs)
admin.site.register(transac)
admin.site.register(income)