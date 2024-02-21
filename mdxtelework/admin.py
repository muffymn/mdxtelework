from django.contrib import admin

from .models import CompletionReport, TeleworkRequest, TimeBlock

# Register your models here.
admin.site.register(CompletionReport)
admin.site.register(TeleworkRequest)
admin.site.register(TimeBlock)
