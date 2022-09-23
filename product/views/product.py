import json

import django_filters
from django.core.exceptions import ObjectDoesNotExist, BadRequest
from django.db import transaction
from django.http import QueryDict
from rest_framework import viewsets, serializers
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from meta.models import Category, Attribute
from product.models import ProductAttributeValue
from product.models.product import Product


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    attribute = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = ProductAttributeValue
        fields = ['value', 'attribute', 'index']

class ProductSerializer(serializers.ModelSerializer):
    attributes = ProductAttributeValueSerializer(many=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'



class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'category']

    def update(self, request, *args, pk=None, **kwargs):
        put = json.loads(request.body)
        try:
            with transaction.atomic():
                item = Product.objects.get(id=pk)
                apply_changes(item, put)
                item = Product.objects.get(id=pk)
                item.validate()
        except (BadRequest, ValidationError) as e:
            return Response({'error':str(e)}, status=400)
        return Response(ProductSerializer(item).data)

    def create(self, request, *args, pk=None, **kwargs):
        put = json.loads(request.body)
        try:
            with transaction.atomic():
                item = Product(
                    category=Category.objects.get(id=put['category']),
                    merchant_id=put.get('merchant_id'),
                    model_id=put.get('model_id'),
                )
                apply_changes(item, put)
                item = Product.objects.get(id=item.id)
                item.validate()
        except (BadRequest, ValidationError) as e:
            return Response({'error':str(e)}, status=400)
        return Response(ProductSerializer(item).data)




def apply_changes(item, data):
    item.model_id = data.get('model_id')
    item.merchant_id = data['merchant_id']
    item.category = Category.objects.get(id=data['category'])
    item.save()

    attribute_value_ids = []
    for input_attribute in data['attributes']:
        lookup_category = item.category
        while lookup_category:
            try:
                attribute = None
                attribute = Attribute.objects.get(category=lookup_category, name=input_attribute['attribute'])
                break
            except ObjectDoesNotExist:
                lookup_category = lookup_category.parent

        if not attribute:
            raise BadRequest(
                f'Attribute {input_attribute["attribute"]} for category {item.category.name} does not exist')
        attribute_value, _ = ProductAttributeValue.objects.get_or_create(product=item, attribute=attribute, index=input_attribute.get('index', 0))
        attribute_value.value = input_attribute['value']
        attribute_value.save()
        attribute_value_ids.append(attribute_value.id)
    ProductAttributeValue.objects.filter(product=item.id).exclude(id__in=attribute_value_ids).delete()
