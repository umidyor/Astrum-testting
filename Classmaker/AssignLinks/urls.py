from django.urls import path
from . import views
app_name = 'Assign'
urlpatterns = [
    path('assign-test/<int:test_id>/<slug:test_description>/', views.AssignLinkView, name='assign'),
    path('assign-test/settings/<int:test_id>/<slug:test_description>/', views.ShowLinks, name='showed-assign'),
    path('assign-test/edit/settings/<int:assign_id>/<slug:test_description>', views.ShowLinksEdit, name='edit-assign'),
    path('assign-link/<int:assign_id>', views.CopyLinks, name='copy-link'),
]

