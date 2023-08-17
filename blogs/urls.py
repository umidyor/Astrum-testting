from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('blog/',create_post,name='blog'),
    path('profile/',user_profile,name='profile'),
    path('profile/<int:post_id>/',view_post,name='posts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)