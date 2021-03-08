from django.contrib import admin
from .models import Products,feeds,MyModel,Post
# Register your models here.

admin.site.register(Products)
admin.site.register(feeds)
admin.site.register(MyModel)

admin.site.register(Post)
