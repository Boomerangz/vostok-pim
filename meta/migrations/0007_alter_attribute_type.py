# Generated by Django 4.1.1 on 2022-09-23 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0006_attribute_created_at_attribute_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='type',
            field=models.CharField(choices=[('string', 'string'), ('text', 'text'), ('integer', 'integer'), ('float', 'float'), ('boolean', 'boolean'), ('datetime', 'datetime'), ('enum', 'enum')], max_length=255),
        ),
    ]
