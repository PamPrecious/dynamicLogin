
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
    path('submit/',views.submit, name="Submit"),
    path('action/',views.action, name="Action"),
    path('act/',views.act, name="Act"),
    path('passred',views.passred, name="Passred"),
    path('editprofile',views.editprofile, name="Editprofile"),
    path('changepassword',views.changepassword, name="Changepassword"),
    
    

]
