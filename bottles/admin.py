from django.contrib import admin
from .models import Bottle

class BottleAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'updated_by','created_at_mtc', 'updated_at_mtc']

    def get_time(self, time):
            import pytz
            fmt = '%Y-%m-%d %H:%M:%S %Z'
            tz = pytz.timezone("US/Mountain")
            dt = time.astimezone(tz)
            return dt.strftime(fmt)

    def created_at_mtc(self, bottle):
        return self.get_time(bottle.created_at)

    def updated_at_mtc(self, bottle):
        return self.get_time(bottle.updated_at)

admin.site.register(Bottle, BottleAdmin)

