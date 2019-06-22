"""Taskq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from web.views import dashboard, CreateTask, sign_up, sign_up_form, login_form, task_list, update_state, delete_task
from django.urls import path
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard),
    path('create_task', CreateTask),
    path('signup/', sign_up),
    path('sign_up_form/',sign_up_form),
    path('loginform/',login_form),
    path('tasklist/',task_list),
    path('update_state/',update_state),
    path('delete_task/',delete_task)

]
