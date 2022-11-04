from django.urls import path

from .views import *

urlpatterns = [
    path('', BottlesListView.as_view(), name='bottle_list'),
    path('bottles/<int:pk>/', BottleUpdateView.as_view(), name='bottle_update'),
]