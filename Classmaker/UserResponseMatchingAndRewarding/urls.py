from django.urls import path
from .views import score
app_name = 'UserScore'
urlpatterns = [
    path('score/<int:user_id>/<slug:user_hashname>', score, name='score'),
]   