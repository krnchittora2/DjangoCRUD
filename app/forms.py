from django import forms
from .models import EmployeeData, RoleData, EmployeeRoleMapData

class EmployeeDataForm(forms.ModelForm):
    class Meta:
        model = EmployeeData
        fields = '__all__'

class RoleDataForm(forms.ModelForm):
    class Meta:
        model = RoleData
        fields = '__all__'

class EmployeeRoleDataForm(forms.ModelForm):
    class Meta:
        model = EmployeeRoleMapData
        fields = '__all__'

