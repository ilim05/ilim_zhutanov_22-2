# Generated by Django 4.1.3 on 2022-11-20 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_category_image_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='text',
            field=models.TextField(null=True),
        ),
    ]