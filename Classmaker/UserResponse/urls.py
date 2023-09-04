from django.urls import path
from .views import answer_question_view, registration_view, previews_questions, startTest
app_name = 'UserResponse'
urlpatterns = [
    path('start/online-test/<int:test_id>/<int:user_id>/<slug:user_hashname>/', answer_question_view, name='responses'),
    path('start/online-test/register/<int:test_id>/', registration_view, name='register'),
    path('previews/online-test/<int:test_id>/<slug:preview_hash>', previews_questions, name='preview'),
    path('start/online-test/<int:test_id>/', startTest, name='start-test')
]