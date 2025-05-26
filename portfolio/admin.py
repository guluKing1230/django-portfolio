from django.contrib import admin
from .models import PersonalInfo, Course, Experience, Project

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'education']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'institution', 'completion_date']
    ordering = ['-completion_date']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'experience_type', 'start_date', 'is_current']
    list_filter = ['experience_type', 'is_current']
    ordering = ['-start_date']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'created_date']
    list_filter = ['featured']
    ordering = ['-created_date']