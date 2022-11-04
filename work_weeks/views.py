from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import WorkWeek

class WorkWeeksListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = WorkWeek
    template_name = 'work_weeks/list.html'