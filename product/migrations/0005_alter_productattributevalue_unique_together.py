# Generated by Django 4.1.1 on 2022-09-23 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0006_attribute_created_at_attribute_updated_at'),
        ('product', '0004_rename_prouctattributevalue_productattributevalue'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productattributevalue',
            unique_together={('product', 'attribute')},
        ),
    ]