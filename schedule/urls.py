from django.urls import path
from . import views

urlpatterns = [
   path('<int:task_id>', views.detail, name='detail'),
   path('create/', views.create, name='create'),
   path('delete/', views.delete, name='delete'),
]
