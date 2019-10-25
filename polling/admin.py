from django.contrib import admin

# Register your models here.
# blogging/admin.py
from django.contrib import admin
from polling.models import Poll

admin.site.register(Poll)
