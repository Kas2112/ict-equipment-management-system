from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = [
        ('ICT_Admin', 'ICT Admin'),
        ('Admin1', 'Admin1'),
        ('Admin2', 'Admin2'),
        ('User', 'User'),
        ('Store', 'Store')
    ]
    role = models.CharField(max_length=20, choices=ROLES)
    department = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

class Equipment(models.Model):
    STATUS = [
        ('Available', 'Available'),
        ('Assigned', 'Assigned'),
        ('Under Maintenance', 'Under Maintenance'),
        ('Decommissioned', 'Decommissioned'),
    ]
    model_number = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100)
    purchase_date = models.DateField()
    warranty_expiry = models.DateField()
    current_status = models.CharField(max_length=20, choices=STATUS, default='Available')
    current_location = models.CharField(max_length=255)
    assigned_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_equipment')
    last_maintenance_date = models.DateField(null=True, blank=True)
    next_maintenance_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

class Request(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('Approved_by_Admin1', 'Approved by Admin1'),
        ('Approved_by_Admin2', 'Approved by Admin2'),
        ('Rejected', 'Rejected'),
        ('Completed', 'Completed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    required_from_date = models.DateField()
    required_to_date = models.DateField()
    purpose = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS, default='Pending')
    admin1_approval_date = models.DateTimeField(null=True, blank=True)
    admin2_approval_date = models.DateTimeField(null=True, blank=True)
    rejection_reason = models.TextField(null=True, blank=True)

class RequestItem(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='items')
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class MaintenanceLog(models.Model):
    TYPE = [
        ('Preventive', 'Preventive'),
        ('Repair', 'Repair'),
    ]
    STATUS = [
        ('Scheduled', 'Scheduled'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    maintenance_type = models.CharField(max_length=20, choices=TYPE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    performed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS, default='Scheduled')

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    table_affected = models.CharField(max_length=100)
    record_id = models.IntegerField()
    old_value = models.TextField(null=True, blank=True)
    new_value = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)