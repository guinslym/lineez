from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include, handler404, handler500

#handler404 = 'applications.websites.views.handler404'
#handler500 = 'applications.websites.views.handler500'
from applications.places.views import (
	PostHomeListView,
	PostDetailView,
	PostCreateView,
	PostDeleteView,
	PostUpdateView
	)




urlpatterns = [
    url(r'^$', PostHomeListView.as_view(), name="posts-home"),
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name="posts-detail"),

    url(r'^create/$', PostCreateView.as_view(), name="posts-create"),
    url(r'^delete/(?P<pk>\d+)/$', PostDeleteView.as_view(), name="posts-delete"),
    url(r'^update/(?P<pk>\d+)/$', PostUpdateView.as_view(), name="posts-update"),
]

#Static files serves with WhiteNoise (pip install WhiteNoise)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
