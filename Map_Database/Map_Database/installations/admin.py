from django.contrib import admin

# Register your models here.
from .models import installation, institution

class InstallationAdmin(admin.ModelAdmin):
    list_display = ['name']
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['name', 'host']
    
admin.site.register(installation, InstallationAdmin)
admin.site.register(institution, InstitutionAdmin)