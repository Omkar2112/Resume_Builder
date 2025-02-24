from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(Profile) 
#admin.site.register(Skill) 


@admin.register(Profile)
class userprofile(admin.ModelAdmin):
    list_display=Profile.DisplayFields
    search_fields=Profile.SearchableFields

@admin.register(Education)
class ueducation(admin.ModelAdmin):
    list_display=Education.DisplayFields
    search_fields=Education.SearchableFields

@admin.register(Project)
class userproject(admin.ModelAdmin):
    list_display=Project.DisplayFields
    search_fields=Project.SearchableFields

@admin.register(Skill)
class userskill(admin.ModelAdmin):
    list_display=Skill.DisplayFields
    search_fields=Skill.SearchableFields