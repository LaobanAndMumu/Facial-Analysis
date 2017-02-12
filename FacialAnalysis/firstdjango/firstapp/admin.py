from django.contrib import admin

# Register your models here.
from .models import Analysis

class AnalysisAdmin(admin.ModelAdmin):
    list_display = ['different','attribute']

admin.site.register(Analysis, AnalysisAdmin)

