from django import forms 
from .models import *

class profile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        labels={'profile_image':''}

class education(forms.ModelForm):
    class Meta:
        model = Education
        fields = "__all__"
class Project(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        widgets = {
            'skill_name': forms.TextInput(attrs={'class': 'autocomplete'}),
        }