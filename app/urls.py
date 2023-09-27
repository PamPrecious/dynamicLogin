
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login, name="Login"),
    path('register',views.register, name="Register"),
    path('dashboard',views.dashboard, name="Dashboard"),
    path('clients',views.clients, name="Clients"),
    path('tasks',views.tasks, name="Tasks"),
    path('users',views.users, name="Users"),
    path('reports',views.reports, name="Reports"),
    path('linked',views.linked, name="Linked"),
    path('adduser',views.adduser, name="Adduser"),
    path('addtask',views.addtask, name="Addtask"),

]
