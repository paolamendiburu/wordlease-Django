from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin, register

from posts.models import Post, Blog

admin.site.register(Post)
admin.site.register(Blog)




#cambiamos el titulo del admin
admin.site.site_header = "Wordplease Admin"
admin.site.site_title = "Wordplease Admin"