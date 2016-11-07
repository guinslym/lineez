from django.contrib import admin
from .models import Post
# Register your models here.
'''
from applications.delivrem.models import Product

admin.site.register(Product)

admin.site.register(Author, AuthorAdmin)
'''

class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'location', 'start_date', 'before_start', 'price', 'description')

#admin.site.register(Post, PostAdmin)
admin.site.register(Post)
