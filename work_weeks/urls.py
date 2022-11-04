from django.urls import path

from .views import *

urlpatterns = [
    # Work Weeks URLS
    path('', WorkWeeksListView.as_view(), name='work_week_list'),

    # Work Week Days URLS
    path('days/<int:pk>/', WorkWeekDayListView.as_view(), name='work_week_day_list')
]