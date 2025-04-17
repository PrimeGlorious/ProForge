from django.contrib import admin
from employers.models import Company, Vacancy


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "website")
    search_fields = ("name", "owner__username")
    list_filter = ("owner",)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ("title", "company", "salary", "location", "created_at")
    search_fields = ("title", "company__name")
    list_filter = ("company", "salary")
    ordering = ("-created_at",)
