from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import WorkWeek, WorkWeekDay

class WorkWeeksListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = WorkWeek
    template_name = 'work_weeks/list.html'
    context_object_name = 'work_weeks'

class WorkWeekDayListView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    model = WorkWeekDay
    template_name = 'work_week_day/list.html'
    context_object_name = 'work_week_days'