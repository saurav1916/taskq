from django.shortcuts import render
from .forms import TaskForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from.models import TaskModel
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
""""
 description : This function renders html page and create a form
 author : Saurav Jindal
 returns : render
 Method allowed : GET
"""""


def dashboard(request):
    obj = TaskForm()
    return render(request, "index.html", {"Forms": obj})


def sign_up(request):
    return render(request, "signup.html")


""""
 description : This creates a Task i.e. it store the entries in database
 author : Saurav Jindal
 returns : render
 Method allowed : POST
"""""


def CreateTask(request):
    data = TaskForm(request.POST)
    data.save()
    return HttpResponseRedirect('/dashboard')


""""
 description : This function creates a user using details.
 author : Saurav Jindal
 returns : HttpResponseRedirect
 Method allowed : POST
"""""


def sign_up_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        User.objects.create_user(username=username, password=password, email=email)
    return HttpResponseRedirect('/dashboard')


""""
 description : This function checks the  user credentials.
 author : Saurav Jindal
 returns : HttpResponseRedirect
 Method allowed : POST
"""""


@csrf_exempt
def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        obj = authenticate(username=username, password=password)
        if obj is not None:
            print("Login Successful")
            return HttpResponseRedirect('/dashboard')


def task_list(request):
    obj = TaskModel.objects.all()
    return render(request, 'tasklist.html', {"task_list":obj})


def update_state(request):
    id = request.GET['id']
    TaskModel.objects.filter(id=id).update(state=request.GET['state'])
    obj = TaskModel.objects.all()
    return render(request, 'tasklist.html', {"task_list": obj})

def delete_task(request):
    id = request.GET['id']
    obj = TaskModel.objects.all()
    TaskModel.objects.all().filter(id=id).update(state = 2)
    return render(request,'tasklist.html',{"task_list": obj})



