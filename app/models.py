from django.db import models

# Create your models here.
class RoleData(models.Model):
    id = models.AutoField(primary_key=True)
    rolename = models.CharField(max_length=255, null=False, blank=False, unique=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    payrange = models.CharField(max_length=255, null=True, blank=True)
    level = models.CharField(max_length=20, null=True, blank=True)


class EmployeeData(models.Model):
    id = models.AutoField(primary_key=True)
    employeename = models.CharField(max_length=255, null=False, blank=False)
    companyid = models.CharField(max_length=255, null=False, blank=False, unique=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)


class EmployeeRoleMapData(models.Model):
    id = models.AutoField(primary_key=True)
    employeeid = models.BigIntegerField(null=False, blank=False)
    roleid = models.BigIntegerField(null=False, blank=False)
    assignedon = models.DateField(null=True, blank=True)
    assignedby = models.CharField(max_length=255, null=True, blank=True)
    lastupdated = models.DateField(auto_now=True)

    