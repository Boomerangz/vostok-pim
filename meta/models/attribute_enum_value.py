from django.db import models


class AttributeEnumValue(models.Model):
    value = models.CharField(max_length=255)
    attribute = models.ForeignKey('Attribute', on_delete=models.PROTECT, related_name='enum_values')
    def __str__(self):
        return self.value