from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import SingleTableView
from django.urls import reverse_lazy

from .models import Bottle
from .tables import BottleTable


class BottlesListView(LoginRequiredMixin, SingleTableView):
    login_url = '/accounts/login/'
    model = Bottle
    template_name = 'bottles/list.html'
    table_class = BottleTable

class BottleUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = Bottle
    template_name = 'edit.html'
    fields = ['start_count', 'end_count']
    context_object_name = 'bottle'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.updated_by = self.request.user.username

        return super(BottleUpdateView, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('bottle_list')