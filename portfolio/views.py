from django.shortcuts import render, redirect
from .models import Project, Skill
# Create your views here.
from .forms import ContactForm
from django.contrib import messages
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
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully! 🎉')
            return redirect('home')
    else:
        form = ContactForm()
    context = {
        'form': form,
    }
    return render(request, 'contact.html', context)
