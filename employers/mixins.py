from django.shortcuts import render


class CompanyOwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user:
            return render(request, "access_denied.html", status=403)
        return super().dispatch(request, *args, **kwargs)


class VacancyOwnerRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.company.owner != request.user:
            return render(request, "access_denied.html", status=403)
        return super().dispatch(request, *args, **kwargs)
