from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, DeleteView,
    UpdateView, RedirectView
    )
# Create your views here.
from .models import Post
from .forms import PostForm

class PostHomeListView(ListView):
    template_name = "post/home.html"
    model = Post


class PostHomeRedirectView(RedirectView):
    url = reverse_lazy('blog-home')


class PostDetailView(DetailView):
    template_name = "post/post.html"
    model = Post


class PostCreateView(CreateView):
    template_name = "post/create.html"
    form_class = PostForm

    def form_valid(self, form):
        """
        Assign the author to the request.user
        """
        #form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post-home')


class PostUpdateView(UpdateView):
    template_name = "post/update.html"
    model = Post
    form_class = PostForm
