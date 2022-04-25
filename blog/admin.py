from django.contrib import admin

from blog.models import Blog, BlogComment, BlogImage

admin.site.register(Blog)
admin.site.register(BlogImage)
admin.site.register(BlogComment)
