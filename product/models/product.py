from django.db import models
from rest_framework.exceptions import ValidationError


class Product(models.Model):
    category = models.ForeignKey('meta.Category', on_delete=models.PROTECT, related_name='products')
    model_id = models.CharField(max_length=255, blank=True, null=True)
    merchant_id = models.CharField(max_length=255)


    def validate(self):
        attributes = self.category.get_attributes()
        attribute_values = self.attributes.all()
        for attribute in attributes:
            attribute_values_count = attribute_values.filter(attribute=attribute).count()
            if attribute.mandatory and attribute_values_count == 0:
                raise ValidationError(f'Attribute {attribute.name} is mandatory')
            if attribute_values_count > attribute.max_values_count:
                raise ValidationError(f'Attribute {attribute.name} has more values than allowed')
            if attribute_values_count < attribute.min_values_count:
                raise ValidationError(f'Attribute {attribute.name} has less values than allowed')
        for attribute_value in attribute_values:
            attribute_value.validate()