from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.Login, name='login'),
    path('logout/', views.logout_admin, name='logout'),
    path('', views.index, name='home'),
    path('view_doctor/', views.view_doctor, name='view_doctor'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('delete_doctor/<int:id>', views.delete_doctor, name='delete_doctor'),
    path('view_patient/', views.view_patient, name='view_patient'),
    path('delete_patient/<int:id>', views.delete_patient, name='delete_patient'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('view_appointment/', views.view_appointment, name='view_appointment'),
    path('delete_appointment/<int:id>', views.delete_appointment, name='delete_appointment'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
]