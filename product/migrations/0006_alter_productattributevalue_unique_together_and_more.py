# Generated by Django 4.1.1 on 2022-09-23 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0007_alter_attribute_type'),
        ('product', '0005_alter_productattributevalue_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productattributevalue',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='productattributevalue',
            name='index',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='productattributevalue',
            unique_together={('product', 'attribute', 'index')},
        ),
    ]