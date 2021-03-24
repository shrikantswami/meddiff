
from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.student_form),
    path('', views.student_list),
    path('form/', views.student_form),
]
