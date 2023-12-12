from django.shortcuts import render,HttpResponse
from .models import Project

# Create your views here.
def portafolio(request):
    projects = Project.objects.all()
    return render(request,"portafolio/portafolio.html",{'projects':projects})