from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views import View
from django.views.decorators.csrf import csrf_protect
from .models import EmployeeData, RoleData, EmployeeRoleMapData
from .forms import EmployeeDataForm, RoleDataForm, EmployeeRoleDataForm


# Create your views here.
@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
    return render(request, 'login.html')

@csrf_protect
def dashboard(request):
    if request.user.is_authenticated:
        employeerolemap = EmployeeRoleMapData.objects.all()
        employeeData = EmployeeData.objects.all()
        roleData = RoleData.objects.all()
        dashboardEntries = []
        for employeerole in employeerolemap:
            tempEmployeeData = EmployeeData.objects.get(pk=employeerole.employeeid)
            tempRoleData = RoleData.objects.get(pk=employeerole.roleid)
            dashboardEntries.append({
                'id': employeerole.id,
                'companyid': tempEmployeeData.companyid,
                'employeename': tempEmployeeData.employeename,
                'gender': tempEmployeeData.gender,
                'rolename': tempRoleData.rolename,
                'department': tempRoleData.department,
                'contact': tempEmployeeData.contact,
                'assignedon': employeerole.assignedon,
                'assignedby': employeerole.assignedby,
                'lastupdated': employeerole.lastupdated
            })
        return render(request, 'dashboard.html', {'dashboardEntries': dashboardEntries, 'employeeData': employeeData, 'roleData': roleData})
    else:
        return redirect('login_view')

@csrf_protect
def save_employee_data(request):
    if (request.user.is_authenticated and request.method == 'POST'):
        form = EmployeeDataForm(request.POST)
        entryId = request.POST.get('id')
        if entryId:
            existingData = get_object_or_404(EmployeeData,pk=entryId)
            form = EmployeeDataForm(request.POST, instance=existingData)
        if form.is_valid():
            try:
                form.save()
                if entryId:
                    messages.success(request, 'Employee Data updated successfully')
                else:
                    messages.success(request, 'Employee Data saved successfully.')
            except Exception as e:
                messages.error(request, 'Error while saving the employee. Please contact support.')
                print(e)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        messages.error(request, 'Invalid Request.')
    return redirect('show_employee')

@csrf_protect
def save_role_data(request):
    if (request.user.is_authenticated and request.method == 'POST'):
        form = RoleDataForm(request.POST)
        entryId = request.POST.get('id')
        if entryId:
            existingData = get_object_or_404(RoleData,pk=entryId)
            form = RoleDataForm(request.POST, instance=existingData)
        if form.is_valid():
            try:
                form.save()
                if entryId:
                    messages.success(request, 'Role Data updated successfully')
                else:
                    messages.success(request, 'Role Data saved successfully.')
            except Exception as e:
                messages.error(request, 'Error while saving the role. Please contact support.')
                print(e)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        messages.error(request, 'Invalid Request.')
    return redirect('show_roles')

@csrf_protect
def save_employee_role_data(request):
    if (request.user.is_authenticated and request.method == 'POST'):
        form = EmployeeRoleDataForm(request.POST)
        entryId = request.POST.get('id')
        if entryId:
            existingData = get_object_or_404(EmployeeRoleMapData,pk=entryId)
            form = EmployeeRoleDataForm(request.POST, instance=existingData)
        if form.is_valid():
            try:
                form.save()
                if entryId:
                    messages.success(request, 'Data updated successfully')
                else:
                    messages.success(request, 'Data saved successfully.')
            except Exception as e:
                messages.error(request, 'Error while saving the data. Please contact support.')
                print(e)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        messages.error(request, 'Invalid Request.')
    return redirect('dashboard')

@csrf_protect
def show_employee(request):
    if request.user.is_authenticated:
        employeeData = EmployeeData.objects.all()
        return render(request, 'employee.html', {'employeeData': employeeData})
    else:
        return redirect('login_view')

@csrf_protect
def show_roles(request):
    if request.user.is_authenticated:
        roleData = RoleData.objects.all()
        return render(request, 'role.html', {'roleData': roleData})
    else:
        return redirect('login_view')

@csrf_protect
def delete_employee_role_data(request, employeeroleid):
    employee_role_data = get_object_or_404(EmployeeRoleMapData, id=employeeroleid)
    if (request.user.is_authenticated and request.method == 'POST'):
        try:
            employee_role_data.delete()
        except:
            print("Error while deleting record.")
        return redirect('dashboard')
    return redirect('dashboard')

class GetEmployeeRoleDataView(View):
    def get(self, request, employeeroleid):
        employee_role_data = get_object_or_404(EmployeeRoleMapData, id=employeeroleid)
        data = {
            'id': employee_role_data.id,
            'employeeid': employee_role_data.employeeid,
            'roleid': employee_role_data.roleid,
            'assignedon': employee_role_data.assignedon,
            'assignedby': employee_role_data.assignedby,
            'lastupdated': employee_role_data.lastupdated,
        }
        return JsonResponse(data)

class GetEmployeeDataView(View):
    def get(self, request, employeeid):
        employee_data = get_object_or_404(EmployeeData, id=employeeid)
        data = {
            'id': employee_data.id,
            'employeename': employee_data.employeename,
            'companyid': employee_data.companyid,
            'gender': employee_data.gender,
            'contact': employee_data.contact,
            'email': employee_data.email,
        }
        return JsonResponse(data)

class GetRoleDataView(View):
    def get(self, request, roleid):
        role_data = get_object_or_404(RoleData, id=roleid)
        data = {
            'id': role_data.id,
            'rolename': role_data.rolename,
            'department': role_data.department,
            'payrange': role_data.payrange,
            'level': role_data.level,
        }
        return JsonResponse(data)
    