from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request,'app/index.html')

def register(request):
    return render(request,'app/register.html')

def dashboard(request):
    complete_tasks = 45
    pending_tasks = 55
    
    context = {
        'complete_tasks': complete_tasks,
        'pending_tasks': pending_tasks,
    }
    
    return render(request,'app/dashboard.html', context)

def clients(request):
    return render(request, 'app/clients.html')

def tasks(request):
    return render(request, 'app/tasks.html')

def users(request):
    return render(request, 'app/users.html')

def reports(request):
    return render(request, 'app/reports.html')

def linked(request):
    return render(request, 'app/linked.html')

def adduser(request):
    return render(request, 'app/adduser.html')

def addtask(request):
    return render(request, 'app/addtask.html')








