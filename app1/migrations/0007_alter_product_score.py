# Generated by Django 5.0.2 on 2024-02-23 11:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_product_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='score',
            field=models.CharField(default=0, max_length=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
