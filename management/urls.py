from django.urls import path
from .views import RegisterView, LoginView, task_detail

urlpatterns = [
    path('users/', RegisterView.as_view()),
    path('token/', LoginView.as_view()),
    path('tasks/<str:task_id>/', task_detail, name='task-detail'), 
]
