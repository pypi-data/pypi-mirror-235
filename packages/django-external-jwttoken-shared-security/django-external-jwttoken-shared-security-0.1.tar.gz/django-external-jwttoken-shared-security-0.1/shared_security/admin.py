from django.contrib import admin
from shared_security import models
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin


class UserExternalDataInline(admin.StackedInline):
    model = models.UserExternalData
    max_num = 1
    can_delete = False

class UserAdmin(AuthUserAdmin):
    inlines = [UserExternalDataInline,]
    
    
# unregister old user admin
admin.site.unregister(get_user_model())
# register new user admin
admin.site.register(get_user_model(), UserAdmin)
