from django.contrib import admin
from .models import Portfolio, Project

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'portfolio_title', 'project')
    search_fields = ('user__first_name', 'user__last_name', 'portfolio_title')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'created_at', 'updated_at')
    search_fields = ('project_name',)

