from django.contrib import admin
from django.utils.translation import gettext as _
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from django.views import generic
from django.http import HttpResponse
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from django.shortcuts import render
from django import forms
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.utils.translation import ugettext_lazy as _
import re
from django.db.models import Q
from ckeditor.fields import RichTextField
# Create your models here.


class Hr(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.CharField(
        max_length=900, verbose_name=_('Description'))
    list_title1 = models.CharField(
        max_length=255, verbose_name=_('List title1 '), blank=True, null=True)
    list_list1 = models.CharField(max_length=900, verbose_name=_(
        'Lists list2'), blank=True, null=True)
    list_list2 = models.CharField(max_length=900, verbose_name=_(
        'Lists list3'), blank=True, null=True)
    list_list3 = models.CharField(max_length=900, verbose_name=_(
        'Lists list4'), blank=True, null=True)
    list_list4 = models.CharField(max_length=900, verbose_name=_(
        'Lists list5'), blank=True, null=True)
    list_list5 = models.CharField(max_length=900, verbose_name=_(
        'Lists list6'), blank=True, null=True)
    list_title2 = models.CharField(
        max_length=255, verbose_name=_('List title2 '), blank=True, null=True)
    list_list6 = models.CharField(max_length=900, verbose_name=_(
        'Lists list1'), blank=True, null=True)
    list_list7 = models.CharField(max_length=900, verbose_name=_(
        'Lists list2'), blank=True, null=True)
    list_list8 = models.CharField(max_length=900, verbose_name=_(
        'Lists list3'), blank=True, null=True)
    list_list9 = models.CharField(max_length=900, verbose_name=_(
        'Lists list4'), blank=True, null=True)
    list_list10 = models.CharField(
        max_length=900, verbose_name=_('Lists list5'), blank=True, null=True)
    list_title3 = models.CharField(
        max_length=255, verbose_name=_('List title3 '), blank=True, null=True)
    list_list11 = models.CharField(
        max_length=900, verbose_name=_('Lists list1'), blank=True, null=True)
    list_list12 = models.CharField(
        max_length=900, verbose_name=_('Lists list2'), blank=True, null=True)
    list_list13 = models.CharField(
        max_length=900, verbose_name=_('Lists list3'), blank=True, null=True)
    list_list14 = models.CharField(
        max_length=900, verbose_name=_('Lists list4'), blank=True, null=True)
    list_list15 = models.CharField(
        max_length=900, verbose_name=_('Lists list5'), blank=True, null=True)

    class Meta:
        verbose_name = _('Human resource')
        verbose_name_plural = _('Human resources')

    def __str__(self):
        return self.title


class Application(models.Model):
    firstname = models.CharField(max_length=255, verbose_name=_('Fristname'))
    lastname = models.CharField(max_length=255, verbose_name=_("Lastname"))
    phone = models.CharField(max_length=255, verbose_name=_('Phone'))

    class Meta:
        verbose_name = _('Application')
        verbose_name_plural = _('Applications')

    def __str__(self):
        return self.firstname


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["firstname", "lastname", "phone", ]
        labels = {
            'fristname': "Овог",
            'lastname': "Нэр",
            'phone': "Утас",
        }

# Problem applicaion view iig Generlic.ListVIew tei hamt ajilluulj neg context-d hiih !


def application(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ApplicationForm()
    return render(request, 'hr/humanresource.html', {'form': form})


class HrList(generic.ListView):
    queryset = Hr.objects.all()
    template_name = 'hr/humanresource.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super(HrList, self).get_context_data(**kwargs)
        context['hr'] = self.get_queryset()
        context['application'] = application
        return context


# Register your models here.

admin.site.register(Hr)
admin.site.register(Application)
