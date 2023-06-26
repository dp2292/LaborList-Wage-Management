"""LaborList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from labor_register import views 

from django.shortcuts import render
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.default_page,name="home_page"),
    # labor CRUD
    path('labor_list/<int:id>/',views.insert_labor,name="labor_update"),
    path('labor_list',views.showlabor,name="Labor_show"),
    path('labor_form/',views.insert_labor,name="Labor_form"),
    path('labor_sort',views.sorted_labor,name="Labor Sort"),
    path('labor_delete/<int:id>/',views.delete_labor,name="Labor Delete"),

    # Supervisr CRUD
    path('supervisor_list/<int:id>/',views.insert_supervisor,name="Supervisor Update"),
    path('supervisor_list',views.showSupervisor,name="Supervisor show"),
    path('supervisor_form/',views.insert_supervisor,name="Supervisor form"),
    path('supervisor_sort',views.sortedsupervisor,name="Supervisor Sort"),
    path('supervisor_delete/<int:id>/',views.delete_supervisor,name="Supervisor Delete"),

    # complex query 
    path('complex_query',views.query_show,name = "Query run"),
    path('run_complex_query',views.raw_query,name = "Query")
]
