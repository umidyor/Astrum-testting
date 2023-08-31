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
    path('delete/<int:post_id>/<slug:post_slug>/',delete_post,name='delete_post'),
    path('edit/<int:post_id>/<slug:post_slug>',edit_post, name='edit_post'),
    path('share_post/<int:post_id>/<slug:post_slug>',share_post,name='share_post'),
    path('media/<path:file_path>', serve_media, name='serve_media'),
    path('redirect_delete',redirects_page,name='redirect_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)