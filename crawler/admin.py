from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class NewUserAdmin(UserAdmin):
    model = User
    fieldsets = ((None, {'fields': ('username', 'password')}),
                 ('Personal info', {
                  'fields': ('first_name', 'last_name', 'reciever')}),
                 ('Permissions', {'fields': ('is_superuser', 'is_staff', 'groups')}))


admin.site.register(User, NewUserAdmin)
