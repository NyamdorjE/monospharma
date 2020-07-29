from django import forms
from django.shortcuts import render
from .models import Application
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.db import models


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["firstname", "lastname", "phone", ]
        labels = {
            'fristname': "Овог",
            'lastname': "Нэр",
            'phone': "Утас",

        }
