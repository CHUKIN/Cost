from django.contrib import admin

# Register your models here.
from .models import Group, Cost

admin.site.register(Group)
admin.site.register(Cost)