# Generated by Django 5.0 on 2024-03-02 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_product_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]