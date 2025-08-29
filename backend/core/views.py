from rest_framework import viewsets, permissions
from .models import User, Equipment, Request, RequestItem, MaintenanceLog, AuditLog
from .serializers import (
    UserSerializer, EquipmentSerializer, RequestSerializer, 
    RequestItemSerializer, MaintenanceLogSerializer, AuditLogSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class RequestItemViewSet(viewsets.ModelViewSet):
    queryset = RequestItem.objects.all()
    serializer_class = RequestItemSerializer

class MaintenanceLogViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceLog.objects.all()
    serializer_class = MaintenanceLogSerializer

class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer