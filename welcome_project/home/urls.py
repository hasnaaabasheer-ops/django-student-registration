from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_student, name='home'),
    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),
]
