from rest_framework import viewsets, serializers

from meta.models import Hierarchy


class HierarchySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hierarchy
        fields = '__all__'


class HierarchyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Hierarchy.objects.all().order_by('id')
    serializer_class = HierarchySerializer
