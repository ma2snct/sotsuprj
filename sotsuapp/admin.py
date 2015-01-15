from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from models import UserProfile
from sotsuapp.models import Relation

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    extra = 0

class MyUserAdmin(UserAdmin):
    inlines = UserAdmin.inlines + [UserProfileInline]

admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)
admin.site.register(Relation)
