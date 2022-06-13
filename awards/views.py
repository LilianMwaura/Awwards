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
def index(request):
    return render(request,'index.html')