from django.shortcuts import render
from django.contrib import messages
from .models import *

# Create your views here.

def home(request):
    profile = Profile.objects.first()
    education = Education.objects.all()
    skills = Skill.objects.all()
    trainings = Training.objects.all()
    achievements = Achievement.objects.all()
    projects = Project.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        Contact.objects.create(
            name=name,
            email=email,
            message=message,
        )
        
        messages.success(request, f"Thank you {name}! Your message has been sent successfully.")
        
    context = {
        "profile": profile,
        "education": education,
        "skills": skills,
        "trainings": trainings,
        "achievements": achievements,
        "projects": projects,
    }

    return render(request, "index.html", context)
