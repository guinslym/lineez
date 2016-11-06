from django.core.management.base import BaseCommand, CommandError

#https://docs.djangoproject.com/en/1.10/howto/custom-management-commands/
from applications.places.models import Post
from mixer.backend.django import mixer


for i in range(10):
    post = mixer.blend(Post)
    post.save()
