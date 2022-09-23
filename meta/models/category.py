from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    hierarchy = models.ForeignKey('Hierarchy', on_delete=models.PROTECT, related_name='categories', null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, related_name='children', null=True, blank=True)
    def __str__(self):
        return self.name


    def get_attributes(self):
        attributes = list(self.attributes.all())
        parent = self.parent
        while parent:
            attributes.extend(parent.attributes.all())
            parent = parent.parent
        return attributes