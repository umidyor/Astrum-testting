from django.urls import path
from . import views
app_name = 'TestingSystem'
urlpatterns = [
    path('main/', views.main_page, name='main-page'),
    path('test/', views.TestViews, name='tests'),
    path('question/<int:test_id>/<slug:test_description>/', views.QuestionView, name='questions'),
    path('test/test/new/', views.home, name='home'),
    path('create-question/multiple/<int:test_id>/<slug:test_description>/', views.CreateQuestionAndMultpleOptions, name='create-multiple'),
    path('edit/multiple/<int:question_id>/<slug:question_description>/', views.EditQuestionAndMultpleOptions, name='question_edit_multiple'),
    path('edit/free-text/<int:question_id>/<slug:question_description>/', views.EditQuestionAndFreeTextOptions, name='question_edit_freetext'),
    path('edit/true-false/<int:question_id>/<slug:question_description>/', views.EditQuestionAndTrueFalseOptions, name='question_edit_truefalse'),
    path('create-question/true-false/<int:test_id>/<slug:test_description>/', views.CreateQuestionAndTrueFalseOptions, name='create-true-false'),
    path('create-question/free-text/<int:test_id>/<slug:test_description>/', views.CreateQuestionAndFreeTextOptions, name='create-free-text'),
]

