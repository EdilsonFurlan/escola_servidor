from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComunicadoViewSet, ParentsViewSet

router = DefaultRouter()
router.register(r'comunicados', ComunicadoViewSet, basename='comunicado')
router.register(r'parents', ParentsViewSet, basename='parent')

urlpatterns = [
    path('', include(router.urls)),
]
