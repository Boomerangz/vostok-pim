import django_filters
from rest_framework import viewsets, serializers

from meta.models import AttributeEnumValue


class AttributeEnumValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeEnumValue
        fields = ['id', 'value', 'attribute']



class AttributeEnumValueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = AttributeEnumValue.objects.all().prefetch_related('attribute').order_by('id')
    serializer_class = AttributeEnumValueSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['attribute']
