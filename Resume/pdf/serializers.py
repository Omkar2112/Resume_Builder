from rest_framework import serializers
from pdf.models import Profile, Education, Project, Skill

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile 
        fields = "__all__"

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education 
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
