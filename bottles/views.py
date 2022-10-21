from django.shortcuts import render
from django.views.generic import ListView

from .models import Bottle

class BottlesListView(ListView):
    model = Bottle
    template_name = 'list.html'
    context_object_name = 'bottles'