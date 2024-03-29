"""mcf_knust_edu_gh_rebuild URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app import views

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
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
