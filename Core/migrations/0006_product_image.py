# Generated by Django 5.0 on 2024-04-26 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_platform_remove_product_image_remove_product_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/product_images/'),
        ),
    ]