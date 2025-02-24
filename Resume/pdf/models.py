

from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _



class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    about_you = models.TextField(max_length=1000)
    
    DisplayFields = ['user', 'name', 'phone', 'email', 'about_you', 'image']
    SearchableFields = ['name', 'email']

    def __str__(self):
        return self.name

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='educations', null=True)
    Degree = models.CharField(max_length=100)
    Degree_College = models.CharField(max_length=100)
    Degree_Location = models.EmailField(max_length=100)
    Master_Degree = models.CharField(max_length=100)
    Master_Degree_College = models.CharField(max_length=100)
    Master_Degree_Location = models.EmailField(max_length=100)

    DisplayFields = ['user', 'Degree','Degree_College','Degree_Location','Master_Degree','Master_Degree_College','Master_Degree_Location']
    SearchableFields = ['Degree', 'Master_Degree']

    def __str__(self):
        return self.Degree

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    Project_Name = models.CharField(max_length=100)
    Project_Details = models.TextField(max_length=1000)

    DisplayFields = ['user', 'Project_Name','Project_Details']
    SearchableFields = ['Project_Name']

    def __str__(self):
        return self.Project_Name
    
class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    skill_names = models.CharField(max_length=100)
    
    DisplayFields = ['user', 'skill_names']
    SearchableFields = ['user']

    def __str__(self):
        return self.skill_names

