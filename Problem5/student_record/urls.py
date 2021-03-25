
from django.urls import path, include
from . import views

urlpatterns = [
    path('create/', views.student_form,name='student_create'),
    path('', views.student_list),
    path('form/', views.student_form,name='student_insert'),
    path('<int:id>/', views.student_form, name='student_update'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'),
    path('search/', views.student_search, name='student_search'),
]
