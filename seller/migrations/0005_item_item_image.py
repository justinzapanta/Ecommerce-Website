# Generated by Django 4.2.5 on 2024-04-01 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0004_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default='Null', upload_to='product/images'),
        ),
    ]