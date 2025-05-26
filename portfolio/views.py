from django.shortcuts import render
from .models import PersonalInfo, Course, Experience, Project

def home(request):
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        personal_info = None
    
    featured_projects = Project.objects.filter(featured=True)[:3]
    recent_experiences = Experience.objects.all()[:3]
    
    context = {
        'personal_info': personal_info,
        'featured_projects': featured_projects,
        'recent_experiences': recent_experiences,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    courses = Course.objects.all().order_by('-completion_date')
    
    context = {
        'courses': courses,
    }
    return render(request, 'portfolio/about.html', context)

def experience(request):
    experiences = Experience.objects.all()
    
    # Process skills for each experience
    for exp in experiences:
        if exp.skills_used:
            exp.skills_list = [skill.strip() for skill in exp.skills_used.split(',')]
        else:
            exp.skills_list = []
    
    context = {
        'experiences': experiences,
    }
    return render(request, 'portfolio/experience.html', context)

def projects(request):
    all_projects = Project.objects.all()
    
    # Process technologies for each project
    for project in all_projects:
        if project.technologies:
            project.tech_list = [tech.strip() for tech in project.technologies.split(',')]
        else:
            project.tech_list = []
    
    context = {
        'projects': all_projects,
    }
    return render(request, 'portfolio/projects.html', context)