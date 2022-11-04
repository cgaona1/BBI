from django.contrib import admin
from .models import WorkWeek, WorkWeekDay

class WorkWeekAdmin(admin.ModelAdmin):
    list_display = ['period_start', 'period_end']

admin.site.register(WorkWeek, WorkWeekAdmin)

class WorkWeekDayAdmin(admin.ModelAdmin):
    pass
admin.site.register(WorkWeekDay, WorkWeekDayAdmin)
