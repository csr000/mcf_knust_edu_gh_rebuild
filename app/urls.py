from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apply/', views.apply, name='apply'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('staff/', views.staff, name='staff'),
    path('event/', views.event, name='event'),
    path('news/', views.news, name='news'),
    path('announcements/', views.announcements, name='announcements'),
    path('publications/', views.publications, name='publications'),
    path('contact/', views.contact, name='contact'),
    path('cohort/<str:id>', views.cohort, name='cohort'),
]
