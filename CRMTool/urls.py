"""
URL configuration for CRMTool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from EmployeeDashboard.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee_form/', employee_form_view, name='employee_form'),
    path('employee_success/', employee_success_view, name='employee_success'), 
    path('employees/', employee_list, name='employee_list'),
    path('employees/<int:pk>/', employee_detail, name='employee_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
