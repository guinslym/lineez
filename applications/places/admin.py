from django.contrib import admin
from .models import Post
# Register your models here.
'''
from applications.delivrem.models import Product

admin.site.register(Product)

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)
'''

admin.site.register(Post)
