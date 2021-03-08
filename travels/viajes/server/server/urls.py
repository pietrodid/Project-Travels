from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.urls import path
from restapi.views import UsuarioViewSet, BoletoViewSet, AsientoViewSet, BusViewSet, TerminalViewSet, TrayectoViewSet   

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('usuario', UsuarioViewSet)
router.register('boleto', BoletoViewSet)
router.register('asiento', AsientoViewSet)
router.register('bus', BusViewSet)
router.register('terminal', TerminalViewSet)
router.register('trayecto', TrayectoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]