from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin, register

from posts.models import Post

admin.site.register(Post)




#cambiamos el titulo del admin
admin.site.site_header = "Wordplease Admin"
admin.site.site_title = "Wordplease Admin"