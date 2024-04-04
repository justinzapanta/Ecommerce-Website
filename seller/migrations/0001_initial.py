# Generated by Django 4.2.5 on 2024-04-04 03:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('cart_item_quantity', models.IntegerField(default=1)),
                ('cart_is_checkedout', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_image', models.ImageField(default=None, upload_to='./main/static/img/products')),
                ('item_name', models.CharField(max_length=200)),
                ('item_type', models.CharField(default=None, max_length=100)),
                ('item_price', models.IntegerField()),
                ('item_quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_total_price', models.IntegerField()),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('cart_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.cart')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='item_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.item'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
