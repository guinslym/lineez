from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'location', 'start_date', 'before_start', 'price', 'description')

#administration
