from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    ListView, DetailView,
    CreateView, DeleteView,
    UpdateView, RedirectView
    )
# Create your views here.
from .models import Post
