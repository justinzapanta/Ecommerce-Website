# Generated by Django 4.2.5 on 2024-04-02 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0012_item_item_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_type',
        ),
    ]
