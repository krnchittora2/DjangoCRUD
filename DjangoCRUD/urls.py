"""
URL configuration for DjangoCRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from django.urls import path
from app import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', LogoutView.as_view(next_page='login_view'), name='logout'),
    path('save_employee_data/', views.save_employee_data, name='save_employee_data'),
    path('save_role_data/', views.save_role_data, name='save_role_data'),
    path('save_employee_role_data/', views.save_employee_role_data, name='save_employee_role_data'),
    path('show_employee/', views.show_employee, name='show_employee'),
    path('show_roles/', views.show_roles, name='show_roles'),
    path('delete_employee_role_data/<int:employeeroleid>/', views.delete_employee_role_data, name='delete_employee_role_data'),
    path('get_employee_role_data/<int:employeeroleid>/', views.GetEmployeeRoleDataView.as_view(), name='get_employee_role_data'),
    path('get_employee_data/<int:employeeid>/', views.GetEmployeeDataView.as_view(), name='get_employee_data'),
    path('get_role_data/<int:roleid>/', views.GetRoleDataView.as_view(), name='get_role_data')
]
