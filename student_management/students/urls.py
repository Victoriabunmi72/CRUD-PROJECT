from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('student/<int:id>/', views.student_detail, name='student_detail'),
    path('student/create/', views.student_create, name='student_create'),
    path('student/update/<int:id>/', views.student_update, name='student_update'),
    path('student/delete/<int:id>/', views.student_delete, name='student_delete'),
]