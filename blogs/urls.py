from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('blog/',create_post,name='blog'),
    path('profile/',user_profile,name='profile'),
    path('profile/<int:post_id>/<slug:post_slug>/',view_post,name='posts'),
    path('profile/<int:post_id>/<slug:post_slug>/edd/', view_post, name='edd_user'),
    path('edds/<slug:post_slug>/',much_posts_edd,name="edds"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)