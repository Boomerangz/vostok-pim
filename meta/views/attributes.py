import django_filters
from django.db.models import Q
from rest_framework import viewsets, serializers
from rest_framework.response import Response

from meta.models import Category, Attribute


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'


class AttributeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Attribute.objects.all().order_by('id')
    serializer_class = AttributeSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['category']

    def list(self, request, *args, **kwargs):
        return super(AttributeViewSet, self).list(request, *args, **kwargs)


    def filter_queryset(self, request, *args, **kwargs):
        queryset = super(AttributeViewSet, self).get_queryset(*args, **kwargs)
        category = self.request.query_params.get('category')
        if category:
            category = Category.objects.get(pk=category)
            category_list = [category]
            while category.parent:
                category = category.parent
                category_list.append(category)
            queryset = queryset.filter(category__in=category_list)
        return queryset
            
