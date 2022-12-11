from rest_framework.viewsets import ModelViewSet
from core.models import Seguimiento
from core.api.serializers import SeguimientoSerializer

class PostApiViewSet(ModelViewSet):
    serializer_class = SeguimientoSerializer
    queryset = Seguimiento.objects.all()