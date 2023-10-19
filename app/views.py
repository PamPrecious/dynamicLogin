from django.shortcuts import render,redirect
from .models import *

# Create your views here.

# recently added clients
def submit(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        service = request.POST.get('service')

        Clients.objects.create(
            name = name,
            email = email,
            contact = contact,
            address = address,
            service = service
        )
        
        clients = Clients.objects.all()
        return redirect("Clients")

#add user in user table
def action(request):
    if request.method == "POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        contact = request.POST.get('contact')

        User.objects.create(
            name = name,
            category = category,
            contact = contact
        )        
        users = User.objects.all()
        return redirect("Users")


#add task in task table
def act(request):
    if request.method == "POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        contact = request.POST.get('contact')
        task = request.POST.get('task')
        client = request.POST.get('clientname')

        Tasks.objects.create(
            name = name,
            category = category,
            contact = contact,
            task = task,
            client = client
        )        
        response = Tasks.objects.all()
        return redirect("Tasks")


def login(request):
    return render(request,'app/index.html')

def register(request):
    return render(request,'app/register.html')
    

def dashboard(request):
    complete_tasks = 45
    pending_tasks = 55
    clients = Clients.objects.all()
    context = {
        'complete_tasks': complete_tasks,
        'pending_tasks': pending_tasks,
        'clients': clients
    }   
    return render(request,'app/dashboard.html', context)

def clients(request):
    clients = Clients.objects.all()
    return render(request, 'app/clients.html',{'clients': clients})

def tasks(request):
    response = Tasks.objects.all()
    context = {
        'response': response
    }
    return render(request, 'app/tasks.html',{'response': response})


def users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'app/users.html',{'users': users})


def reports(request):
    return render(request, 'app/reports.html')

def linked(request):
    return render(request, 'app/linked.html')

def adduser(request):
    return render(request, 'app/adduser.html')

def addtask(request):
    user = User.objects.all()
    client = Clients.objects.all()
    return render(request, 'app/addtask.html' , {'clients': client , 'users':user})

def editprofile(request):
    return render(request, 'app/editprofile.html')

def changepassword(request):
    return render(request, 'app/changepassword.html')

def passred(request):
    return render(request, 'app/passred.html')






