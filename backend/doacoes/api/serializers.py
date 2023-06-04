from rest_framework import serializers
from backend.doacoes.models import Doacao


class DoacaoSerializer(serializers.ModelSerializer):

    doador = serializers.ReadOnlyField(
        default=serializers.CurrentUserDefault())

    class Meta:
        model = Doacao
        fields = ['id', 'doador', 'volume', 'is_done', 'created']
