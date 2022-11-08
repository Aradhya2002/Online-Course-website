from django.contrib import admin
from .models import saveregister, video, teacher
# Register your models here.
@admin.register(saveregister)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in saveregister._meta.get_fields()]

@admin.register(teacher)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in teacher._meta.get_fields()]
admin.site.register(video)