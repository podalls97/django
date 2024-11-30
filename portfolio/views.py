from django.shortcuts import render
from .models import Project, Skill

def index(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    return render(request, 'portfolio/index.html', {
        'projects': projects,
        'skills': skills,
    })
