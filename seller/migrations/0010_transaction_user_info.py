# Generated by Django 4.2.5 on 2024-04-10 04:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seller', '0009_alter_transaction_transaction_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='user_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
