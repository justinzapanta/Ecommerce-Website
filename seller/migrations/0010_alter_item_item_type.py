# Generated by Django 4.2.5 on 2024-04-02 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0009_item_item_type_alter_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.CharField(default='', max_length=100),
        ),
    ]
