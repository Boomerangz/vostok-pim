# Generated by Django 4.1.1 on 2022-09-22 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attribute',
            name='max_capacity',
        ),
        migrations.AddField(
            model_name='attribute',
            name='max_values_count',
            field=models.IntegerField(default=1),
        ),
    ]