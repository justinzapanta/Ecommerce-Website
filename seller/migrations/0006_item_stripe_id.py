# Generated by Django 4.2.5 on 2024-04-09 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_rename_cart_item_price_cart_cart_item_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='stripe_id',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]