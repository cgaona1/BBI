from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import SingleTableView

from .models import Bottle
from .tables import BottleTable


class BottlesListView(LoginRequiredMixin, SingleTableView):
    login_url = '/accounts/login/'
    model = Bottle
    template_name = 'list.html'
    table_class = BottleTable