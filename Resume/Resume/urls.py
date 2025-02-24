"""
URL configuration for Resume project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from pdf import views
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
   
    path('',views.LoginPage,name='login'),
    path('home/', views.home, name='home'),
    path('logout/',views.logout_view, name='logout'),
    path('signup/',views.SignupPage,name='signup'),
    path('create_resume/', views.profile, name='create_resume'),
    path('profile/',views.profile, name='profile'),
    path('degree/',views.education,name="degree"),
    path('project/',views.projects,name='project'),
    path('user-details/', views.user_detail, name='user_details'),
    path('skill/',views.skills,name='skill'),
    path('<int:id>/',views.resume,name="resume"),
    path("pdf/v1/",include('pdf.urls')), 
    path('skill-autocomplete/', views.skill_autocomplete, name='skill_autocomplete'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

