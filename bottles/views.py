from django.shortcuts import render
from django.views.generic import ListView
from django_tables2 import SingleTableView

from .models import Bottle
from .tables import BottleTable

class BottlesListView(SingleTableView):
    model = Bottle
    template_name = 'list.html'
    table_class = BottleTable