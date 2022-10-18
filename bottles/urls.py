from django.urls import path

from .views import *

urlpatterns = [
    path('', BottlesListView.as_view(), name='bottles_list'),
]