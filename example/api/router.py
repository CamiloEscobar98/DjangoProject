from rest_framework.routers import DefaultRouter
from example.api.views import PostApiViewSet, VulnerabilityApiViewSet

router = DefaultRouter()

router.register(prefix='posts', basename='posts', viewset=PostApiViewSet)
router.register(prefix='vulnerabilities', basename='vulnerabilities', viewset=VulnerabilityApiViewSet)