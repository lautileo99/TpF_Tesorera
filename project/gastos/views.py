from django.shortcuts import render
from .models import Project

# Create your views here.
def gastos(request):
    projects = Project.objects.all()
    return render(request,"gastos/gastos.html",{'projects':projects})