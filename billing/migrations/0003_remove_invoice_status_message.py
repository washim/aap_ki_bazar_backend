# Generated by Django 3.2.11 on 2022-01-21 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_remove_order_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='status_message',
        ),
    ]