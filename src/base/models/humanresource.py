from django.contrib import admin
from django.utils.translation import gettext as _
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from django.views.generic.edit import ModelFormMixin
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
from django.views.generic import ListView, CreateView, UpdateView
from ckeditor.fields import RichTextField
# Create your models here.


class Hr(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.CharField(
        max_length=900, verbose_name=_('Description'))

    class Meta:
        verbose_name = _('Human resource')
        verbose_name_plural = _('Human resources')

    def __str__(self):
        return self.title


class ListTitle(models.Model):
    text = models.CharField(verbose_name=_('Text'), max_length=128)
    open_job = models.ForeignKey(Hr, verbose_name=_(
        'Open job'), on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = _('List title ')
        verbose_name_plural = _('List titles')

    def __str__(self):
        return u'{0}'.format(self.text)


class ListItem(models.Model):
    text = models.CharField(verbose_name=_('Text'), max_length=128)
    list_title = models.ForeignKey(ListTitle, verbose_name=_(
        'List title'), on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = _('List Item ')
        verbose_name_plural = _('List Items')

    def __str__(self):
        return u'{0}'.format(self.text)


class Application(models.Model):
    firstname = models.CharField(max_length=255, verbose_name=_('Firstname'))
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


class HrList(ListView, ModelFormMixin):
    model = Hr
    form = ApplicationForm
    template_name = 'hr/humanresource.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        # Explicitly states what get to call:
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # When the form is submitted, it will enter here
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save()
            # Here ou may consider creating a new instance of form_class(),
            # so that the form will come clean.

        # Whether the form validates or not, the view will be rendered by get()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HrList, self).get_context_data(**kwargs)
        context['hr'] = self.get_queryset()
        return context


# Register your models here.
admin.site.register(Hr)
admin.site.register(Application)
admin.site.register(ListItem)
admin.site.register(ListTitle)
