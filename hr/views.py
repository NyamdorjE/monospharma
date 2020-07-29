from django.shortcuts import render
from .models import Hr
from .forms import ApplicationForm
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _


class HrList(generic.ListView):
    queryset = Hr.objects.all()
    template_name = 'hr/humanresource.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(HrList, self).get_context_data(**kwargs)
        context['hr'] = self.get_queryset()
        return context


def application(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ApplicationForm()
    return render(request, 'hr/humanresource.html', {'form': form})
