from django.urls import path
from rest_framework.routers import DefaultRouter
from .core.views import PersonViewSet
router = DefaultRouter()
router.register(r"people", PersonViewSet, basename="people")

urlpatterns = router.urls