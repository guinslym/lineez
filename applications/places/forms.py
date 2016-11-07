from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        exclude = [
            'titre', 'location', 'start_date',
            'before_date', 'price', 'description'
        ]

#administration
