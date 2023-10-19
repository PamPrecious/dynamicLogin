from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Clients)
class Precious(admin.ModelAdmin):
    list_display = Clients.clients_view

@admin.register(Dashboard)
class Precious(admin.ModelAdmin):
    list_display = Dashboard.dashboard_view

@admin.register(User)
class Precious(admin.ModelAdmin):
    list_display = User.user_view

@admin.register(Tasks)
class Precious(admin.ModelAdmin):
    list_display = Tasks.tasks_view    