from django.shortcuts import render

# Create your views here.
from django.template import loader
from .models import Installation, Institution
from django.http import Http404
from django.http import HttpResponse

def index(request):
    installation = Installation.objects.all()
    return render(request, 'installations/index.html', {
        'installation': installation
    })

def installations(request, institution_name):
    return HttpfResponse('This is the newest afilliated institution in the <b>%s</b> installation' % institution_name)

def Map(request):
    install_list = Installation.objects.all()
    institute_list = Institution.objects.all()
    d = dict(
        install_list = install_list,
        institute_list = institute_list,
    )
    
    return render(request, 'installations/map.html', d)

def institutions(request, installation):
    Institution = institution.objects.get(host=installation.name)
    return render(request, 'installations/institution.html', {
        "Institution": Institution,
    })

def landingpage(request):
    return render(request, 'installations/home.html')
    