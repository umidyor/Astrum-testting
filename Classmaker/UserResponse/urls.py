from django.urls import path
from .views import answer_question_view, registration_view, previews_questions, startTest
app_name = 'UserResponse'
urlpatterns = [
    path('start/online-test/<int:assign_id>/<int:user_id>/<slug:assign_slug>/', answer_question_view, name='responses'),
    path('start/online-test/register/<int:assign_id>/<slug:assign_slug>/', registration_view, name='register'),
    path('previews/online-test/<int:test_id>/<slug:preview_hash>', previews_questions, name='preview'),
    path('start/online-test/<int:assign_id>/<slug:assign_slug>/', startTest, name='start-test')
]