from rest_framework import viewsets

from backend.doacoes.api.serializers import DoacaoSerializer
from backend.doacoes.models import Doacao


class DoacoesViewSet(viewsets.ModelViewSet):

    queryset = Doacao.objects.all()

    def get_serializer_class(self):
        return DoacaoSerializer
