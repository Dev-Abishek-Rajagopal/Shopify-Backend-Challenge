from django.contrib import admin

from .models import RepUser, ImgRep, ImgCart
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UserAdminConfig(UserAdmin):

    search_fields = ("email","username","firstname","lastname")
    list_filter = ("email","username","firstname","lastname","is_staff","is_active","is_superuser")
    list_display = ("email","username","firstname","lastname","is_staff","is_active","is_superuser")

    fieldsets = ( ("Basic Information",{ "fields" : ("email","username","firstname","lastname")} ),
                  ("Permission Information",{"fields": ("is_staff","is_active","is_superuser")}) )

    add_fieldsets = (
        (None, {
        "classes" : ("wide",),
        "fields" : ("email","username","firstname","lastname","password1","password2","is_staff","is_active")
    }),)

class ImgRepAdminConfig(admin.ModelAdmin):

    # search_fields = ("email","username","firstname","lastname")
    # list_filter = ("email","username","firstname","lastname","is_staff","is_active","is_superuser")
    list_display = ("img","name","user","scope","access","price","discount","color_palette")

admin.site.register(RepUser, UserAdminConfig)
admin.site.register(ImgRep, ImgRepAdminConfig)
admin.site.register(ImgCart)



