from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, EquipmentViewSet, RequestViewSet, 
    RequestItemViewSet, MaintenanceLogViewSet, AuditLogViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'requests', RequestViewSet)
router.register(r'requestitems', RequestItemViewSet)
router.register(r'maintenance', MaintenanceLogViewSet)
router.register(r'audit', AuditLogViewSet)

urlpatterns = router.urls