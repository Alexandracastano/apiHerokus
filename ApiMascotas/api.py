from .models import Mascotas
from rest_framework import viewsets,  permissions

from .serializers import MascotasSerializer

class MascotasviewSet(viewsets.ModelViewSet):
    queryset = Mascotas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MascotasSerializer