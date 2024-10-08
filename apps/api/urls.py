from rest_framework import routers
from django.urls import include, path
from api.viewsets import UsuarioViewSet, PorteiroViewSet, VisitanteViewSet

router = routers.DefaultRouter()

router.register(r'usuarios',UsuarioViewSet)
router.register(r'porteiros',PorteiroViewSet)
router.register(r'visitantes',VisitanteViewSet)

urlpatterns = [
    path('', include(router.urls))
]