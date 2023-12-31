# Generated by Django 5.0 on 2024-01-05 05:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='totalInPence',
            new_name='total_in_pence',
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='customers.customer'),
        ),
    ]
