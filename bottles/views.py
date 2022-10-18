from django.shortcuts import render
from django.views.generic import TemplateView

class BottlesListView(TemplateView):
    template_name = 'list.html'