from django.forms import modelformset_factory
from django.views.decorators.http import require_GET
from django.db.models.functions import Lower
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from pdf.models import *
from rest_framework import viewsets
from pdf.serializers import EducationSerializer, ProfileSerializer, ProjectSerializer,SkillSerializer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

@login_required(login_url='login')
def home(request):
    logged_in_username = request.session.get('logged_in_username', None)
    print("Logged in email:", logged_in_username)
    return render(request, 'home.html')

def logout_view(request):
    # Clear session data
    if 'logged_in_username' in request.session:
        del request.session['logged_in_username']
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    user = request.user
    profile_instance = user.profile.first() if hasattr(user, 'profile') else None
    logged_in_username = request.session.get('logged_in_username', None)

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        about_you = request.POST.get('about_you')
        image = request.FILES.get('image')

        if profile_instance:
            # Update existing profile instance
            profile_instance.name = name
            profile_instance.phone = phone
            profile_instance.email=email
            profile_instance.about_you = about_you
            if image:
                profile_instance.image = image
            profile_instance.save()
        else:
            # Create new profile instance
            profile_instance = Profile.objects.create(user=user, name=name, phone=phone, email=email,about_you=about_you, image=image)
        
        return redirect('degree')

    return render(request, 'profile_form.html', {'profile': profile_instance, 'logged_in_username': logged_in_username})

@login_required(login_url='login')
def projects(request):
    if request.method == "POST":
        Project_Name = request.POST.get("Project_Name", "")
        Project_Details = request.POST.get("Project_Details", "")
        
        # Get the currently logged-in user
        user = request.user

        # Check if project exists
        project = Project.objects.filter(user=user).first()
        if project:
            # Update existing project
            project.Project_Name = Project_Name
            project.Project_Details = Project_Details
            project.save()
        else:
            # Create new project instance
            project = Project.objects.create(user=user, Project_Name=Project_Name,Project_Details=Project_Details)
        
        return redirect('skill')

    return render(request, 'project.html')

@login_required(login_url='login')
def education(request):
    if request.method =='POST':
        
        Degree = request.POST.get('Degree', "")
        Degree_College = request.POST.get('Degree_College', "")
        Degree_Location = request.POST.get('Degree_Location', "")
        Master_Degree = request.POST.get('Master_Degree', "")
        Master_Degree_College = request.POST.get('Master_Degree_College', "")
        Master_Degree_Location = request.POST.get('Master_Degree_Location', "")
        
        # Get the currently logged-in user
        user = request.user

        # Check if education exists
        education = Education.objects.filter(user=user).first()
        if education:
            # Update existing education
            education.Degree = Degree
            education.Degree_College = Degree_College
            education.Degree_Location = Degree_Location
            education.Master_Degree = Master_Degree
            education.Master_Degree_College = Master_Degree_College
            education.Master_Degree_Location = Master_Degree_Location
            education.save()
        else:
            # Create new education instance
            education = Education.objects.create(user=user, Degree=Degree, Degree_College=Degree_College, Degree_Location=Degree_Location, Master_Degree=Master_Degree, Master_Degree_College=Master_Degree_College, Master_Degree_Location=Master_Degree_Location)
        
        return redirect('project')  # Assuming you want to redirect to the project view after saving education
    return render(request, 'degree.html')


@login_required(login_url='login')
def skills(request):
  
   

    if request.method == 'POST':
        # Assuming skill names are submitted as a list or comma-separated string in the form
        skill_names = request.POST.get('skills_names', "")  # Split the string into a list of skill names

        user = request.user

        skills = Skill.objects.filter(user=user).first()

        if skills:
            # Update existing education
            skills.skill_names = skill_names
            skills.save()
        else:
             skills = Skill.objects.create(user=user, skill_names=skill_names)

 

        return redirect('user_details')  # Redirect to profile or any other desired view

    return render(request, 'skills.html')

def skill_autocomplete(request):
    term = request.GET.get('term', '')
    matching_skills = Skill.objects.filter(skill_names__istartswith=term).values_list('skill_names', flat=True)
    return JsonResponse(list(matching_skills), safe=False)

def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    return render(request, "resume.html", {'user_profile': user_profile})
def SignupPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if not (email and password1 and first_name and last_name):
            return HttpResponse("All fields are required!")

        if User.objects.filter(email=email).exists():
            return HttpResponse("This email address is already registered. Please use a different email.")
        
        my_user = User.objects.create_user(username=email, email=email, password=password1)
        my_user.first_name = first_name
        my_user.last_name = last_name
        my_user.save()
        request.POST = None
        signup_successful = True

        if signup_successful:
            messages.success(request, "Signup successful! You can now log in.")
            return redirect('login')
        else:
            messages.error(request, "Signup failed. Please try again.")
            return redirect('signup')

    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if username and password are provided
        if not email:
            messages.error(request, "Username is required.")
            return render(request, 'login.html')
        if not password:
            messages.error(request, "Password is required.")
            return render(request, 'login.html')

        # Check if user exists in the database
        user = User.objects.filter(email=email).first()
        if not user:
            messages.error(request, "User not found. Please sign up.")
            return redirect('signup')

        # Check if password is correct
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            request.session['logged_in_username'] = email
            messages.success(request, "Login successful.")
            return redirect('home')
        else:
            messages.error(request, "Incorrect password. Please try again.")
            return render(request, 'login.html')

    return render(request, 'login.html')


def user_detail(request):
    # Get the currently logged-in user
    user = request.user

    # Fetch profile details
    profile = Profile.objects.get(user=user)

    # Fetch education details
    education = Education.objects.filter(user=user)

    # Fetch project details
    projects = Project.objects.filter(user=user)

    # Fetch skills 
    skills = Skill.objects.filter(user=user)

    return render(request, 'user_details.html', {'profile': profile, 'education': education, 'projects': projects,'skills':skills })