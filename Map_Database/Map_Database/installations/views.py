from django.shortcuts import render

# Create your views here.
from django.template import loader
from .models import installation, institution
from django.http import Http404
from django.http import HttpResponse

def index(request):
    Installation = installation.objects.all()
    return render(request, 'installations/index.html', {
        'Installation': Installation
    })

def installations(request, institution_name):
    return HttpfResponse('This is the newest afilliated institution in the <b>%s</b> installation' % institution_name)

def Map(request):
    inst_list = installation.objects.all()
    d = dict(inst_list = inst_list)
    
    return render(request, 'installations/map.html', d)

def institutions(request, installation):
    Institution = institution.objects.get(host=installation.name)
    return render(request, 'installations/institution.html', {
        "Institution": Institution,
    })

def landingpage(request):
    return render(request, 'installations/home.html')
    