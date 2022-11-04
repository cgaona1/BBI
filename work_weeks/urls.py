from django.urls import path

from .views import *

urlpatterns = [
    path('', WorkWeeksListView.as_view(), name='work_week_list'),
]