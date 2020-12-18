from django.contrib import admin

# Register your models here.
from help_desk import models


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.ClaimModel, UserAdmin)
admin.site.register(models.CommentModel, UserAdmin)
