from datetime import datetime

from django.core.exceptions import BadRequest
from django.db import models
from rest_framework.exceptions import ValidationError

import meta


class ProductAttributeValue(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT, related_name='attributes')
    value = models.CharField(max_length=255)
    attribute = models.ForeignKey('meta.Attribute', on_delete=models.PROTECT)
    index = models.IntegerField(default=0)

    class Meta:
        unique_together = ('product', 'attribute', 'index')

    def __str__(self):
        return f'{self.attribute.name} - {self.value}'


    def validate(self):
        if self.attribute.mandatory:
            if not self.value:
                raise ValidationError(f'Attribute {self.attribute.name} is mandatory')
        if self.attribute.type == meta.models.ATTRIBUTE_TYPE_ENUM:
            if self.value not in [v.value for v in self.attribute.enum_values.all()]:
                raise ValidationError(f'Value "{self.value}" of attribute "{self.attribute.name}" is not in list of valid values')
        elif self.attribute.type == meta.models.ATTRIBUTE_TYPE_STRING:
            pass
        elif self.attribute.type == meta.models.ATTRIBUTE_TYPE_INTEGER:
            try:
                int(self.value)
            except ValueError:
                raise ValidationError(f'Value {self.value} is not integer')
        elif self.attribute.type == meta.models.ATTRIBUTE_TYPE_FLOAT:
            try:
                float(self.value)
            except ValueError:
                raise ValidationError(f'Value {self.value} is not float')
        elif self.attribute.type == meta.models.ATTRIBUTE_TYPE_BOOLEAN:
            if self.value not in ['true', 'false']:
                raise ValidationError(f'Value {self.value} is not boolean')
        elif self.attribute.type == meta.models.ATTRIBUTE_TYPE_DATETIME:
            try:
                datetime.strptime(self.value, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                raise ValidationError(f'Value {self.value} is not datetime')
        elif self.attribute.type == meta.models.ATTRIBUTE_TYPE_TEXT:
            pass
        else:
            raise ValidationError(f'Unknown attribute type {self.attribute.type}')
