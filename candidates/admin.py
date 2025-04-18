from django.contrib import admin
from candidates.models import Candidate, Application


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "current_role")
    search_fields = ("username", "first_name", "last_name")
    list_filter = ("current_role",)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("candidate", "vacancy", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("candidate__username", "vacancy__title")
    ordering = ("-created_at",)
