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

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    form = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':  
        
        
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = request.user
            prof.save()
            return redirect ('index')
        
        else:
            form = ProfileForm()
    return render(request, 'update-profile.html', {'form': form})

@login_required(login_url='/accounts/login/')
def profile(request,pk):
    
    user = User.objects.get(pk = pk)
    profiles = Profile.objects.filter(user = user).all()
    current_user = request.user
    projects = Project.objects.filter(user = user).all()
    return render(request,'profile.html',{"current_user":current_user,"projects":projects, "user":user, "profiles":profiles})

@login_required
def search_results(request):
    
  if 'search_user' in request.GET and request.GET["search_user"]:
    search_term = request.GET.get('search_user')
    searched_projects = Project.search_project(search_term)
    message = f"{search_term}"
    return render(request,'search.html',{"message":message,"users":searched_projects})
  else:
    message="You haven't searched for any term."  
    projects = Project.objects.all()
    return render(request,'search.html',{"message":message,"users":searched_projects,"projects":projects}) 
    