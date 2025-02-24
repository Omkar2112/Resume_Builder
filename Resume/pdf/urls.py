
from django.contrib import admin
from django.urls import include, path
from pdf.views import EducationViewSet, ProfileViewSet, ProjectViewSet, SkillViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'educations', EducationViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)

urlpatterns = [
   path('',include(router.urls))
   
]