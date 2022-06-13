from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import Project, Profile, Review
from .forms import ProfileForm, ProjectForm, RateForm
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer, ProfileSerializer

# Create your views here.
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user = request.user
        profile =Profile.objects.get(user=current_user)
        
    except ObjectDoesNotExist:
        return redirect('update_profile')
    profiles = Profile.objects.filter(user_id = current_user.id).all()
    projects = Project.objects.all().order_by('-posted_at')
    return render(request, 'index.html',{"profiles": profiles, "projects":projects})