from rest_framework.routers import DefaultRouter
from example.api.views import VulnerabilityApiViewSet

router = DefaultRouter()
router.register(prefix='vulnerabilities', basename='vulnerabilities', viewset=VulnerabilityApiViewSet)