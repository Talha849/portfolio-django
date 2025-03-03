from django.shortcuts import render
from .models import Project, Skill
# Create your views here.
def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    context = {
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'index.html', context)

# def projects(request):
#     projects = Project.objects.all()
#     context = {
#         'projects': projects,
#     }
#     return render(request, 'projects.html', context)