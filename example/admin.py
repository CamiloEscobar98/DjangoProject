from django.contrib import admin
from example.models import Vulnerability

@admin.register(Vulnerability)
# Register your models here.
class VulnerabilityAdmin(admin.ModelAdmin):
    list_display = ['id', 'code']
