from rest_framework import serializers
from .models import User, Equipment, Request, RequestItem, MaintenanceLog, AuditLog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'department', 'phone']

class EquipmentSerializer(serializers.ModelSerializer):
    assigned_to = UserSerializer(read_only=True)
    class Meta:
        model = Equipment
        fields = '__all__'

class RequestItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestItem
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    items = RequestItemSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Request
        fields = '__all__'

class MaintenanceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceLog
        fields = '__all__'

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'