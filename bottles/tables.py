import django_tables2 as tables
from .models import Bottle

class BottleTable(tables.Table):
    class Meta:
        model = Bottle
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = ['name', 'start_count', 'end_count']