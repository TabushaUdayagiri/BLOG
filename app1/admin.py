from django.contrib import admin
from app1.models import post

# Register your models here.


# @admin.register(blog)
# class blogadmin(admin.ModelAdmin):
#     list_display = ['title','description']



@admin.register(post)
class postadmin(admin.ModelAdmin):
    list_display = ['title','description','posted_date','user_id']
