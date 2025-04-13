from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView

from employers.forms import CompanyForm
from employers.models import Company, Vacancy


class CompanyDetailView(DetailView):
    model = Company
    context_object_name = "company"
    template_name = "employers/company_detail.html"


class VacanciesListView(ListView):
    model = Vacancy
    context_object_name = "vacancies"
    template_name = "employers/vacancies_list.html"
    paginate_by = 7

    def get_queryset(self):
        queryset = Vacancy.objects.all().order_by("-created_at")
        text = self.request.GET.get("text", "")
        salary = self.request.GET.get("salary")
        location = self.request.GET.get("location")
        company = self.request.GET.get("company")
        sort_by = self.request.GET.get("sort")

        if text:
            return queryset.filter(
                Q(title__icontains=text) | Q(description__icontains=text)
            )
        if salary:
            queryset = queryset.filter(salary__gte=salary)
        if location:
            queryset = queryset.filter(location__icontains=location)
        if company:
            queryset = queryset.filter(company__name=company)

        if sort_by == "salary_desc":
            queryset = queryset.order_by("-salary")
        elif sort_by == "salary_asc":
            queryset = queryset.order_by("salary")
        elif sort_by == "date":
            queryset = queryset.order_by("-created_at")

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VacanciesListView, self).get_context_data(**kwargs)

        text = self.request.GET.get("text", "")

        context["search_query"] = text
        context["filter"] = {
            "salary": self.request.GET.get("salary", ""),
            "title": self.request.GET.get("title", ""),
            "location": self.request.GET.get("location", ""),
            "company": self.request.GET.get("company", ""),
            "sort": self.request.GET.get("sort", ""),
        }
        context["companies"] = Company.objects.all()

        return context


class VacanciesDetailView(DetailView):
    model = Vacancy
    context_object_name = "vacancy"
    template_name = "employers/vacancies_detail.html"


class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = "employers/company_form.html"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("employers:company_detail", kwargs={"pk": self.object.pk})
