from django.urls import path
from .views import answer_question_view, registration_view
urlpatterns = [
    path('<int:test_id>/<int:user_id>/<slug:user_name>', answer_question_view, name='responses'),
    path('register/', registration_view, name='register')
]