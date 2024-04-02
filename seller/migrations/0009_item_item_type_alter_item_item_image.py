# Generated by Django 4.2.5 on 2024-04-02 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0008_alter_item_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(default=None, upload_to='./main/static/img/products'),
        ),
    ]
