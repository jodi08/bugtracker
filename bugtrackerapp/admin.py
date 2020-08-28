from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from bugtrackerapp.models import New_User, Ticket

# Register your models here.
admin.site.register(Ticket)
admin.site.register(New_User, UserAdmin)

