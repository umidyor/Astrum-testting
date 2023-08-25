from django.urls import path
from . import views
app_name = 'TestingSystem'
urlpatterns = [
    path('test/', views.TestViews, name='tests'),
    path('test/test/new/', views.home, name='home'),
    path('create-question/multiple/<int:test_id>/<slug:test_description>', views.CreateQuestionAndMultpleOptions, name='create-multiple'),
    path('edit/<int:question_id>/', views.EditQuestionAndMultpleOptions, name='question_edit'),
    path('question/<int:pk>/delete/', views.DeleteQuestionView.as_view(), name='delete_question'),
    path('test/<int:pk>/delete/', views.DeleteTestView.as_view(), name='delete_test'),
    path('create-question/true-false/<int:test_id>/<slug:test_description>', views.CreateQuestionAndTrueFalseOptions, name='create-true-false'),
    path('create-question/free-text/<int:test_id>/<slug:test_description>', views.CreateQuestionAndFreeTextOptions, name='create-free-text'),
]

