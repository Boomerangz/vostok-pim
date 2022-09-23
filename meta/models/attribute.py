from django.db import models



ATTRIBUTE_TYPE_ENUM = 'enum'
ATTRIBUTE_TYPE_STRING = 'string'
ATTRIBUTE_TYPE_INTEGER = 'integer'
ATTRIBUTE_TYPE_FLOAT = 'float'
ATTRIBUTE_TYPE_BOOLEAN = 'boolean'
ATTRIBUTE_TYPE_DATETIME = 'datetime'
ATTRIBUTE_TYPE_TEXT = 'text'


ATTRIBUTE_TYPES = (
    ('string', ATTRIBUTE_TYPE_STRING),
    ('text', ATTRIBUTE_TYPE_TEXT),
    ('integer', ATTRIBUTE_TYPE_INTEGER),
    ('float', ATTRIBUTE_TYPE_FLOAT),
    ('boolean', ATTRIBUTE_TYPE_BOOLEAN),
    ('datetime', ATTRIBUTE_TYPE_DATETIME),
    ('enum', ATTRIBUTE_TYPE_ENUM),
)

class Attribute(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    type = models.CharField(max_length=255, choices=ATTRIBUTE_TYPES)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='attributes')
    max_values_count = models.IntegerField(default=1)
    min_values_count = models.IntegerField(default=1)
    mandatory = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.category.name} - {self.name}'


