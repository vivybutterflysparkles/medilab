
from django.contrib import admin
from django.urls import path
from medilabapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('start/', views.start, name='start'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('department/', views.department, name='department'),
    path('doctors/', views.doctors, name='doctors'),
    path('contact/', views.contact, name='contact'),
    path('patient/', views.patient, name='patient'),
    path('appointment/', views.appointment, name='appointment'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
]
