from rest_framework.serializers import ModelSerializer
from core.models import Seguimiento

class SeguimientoSerializer(ModelSerializer):
    class Meta:
        model = Seguimiento
        fields = ['id','matrona','recien_nacido','peso_diario','tolerancia_alimentaria','orina','deposicion','sector_sala','n_cupo','fecha','observacion']