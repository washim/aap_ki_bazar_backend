# Generated by Django 3.2.11 on 2022-02-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0003_remove_invoice_status_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='availability',
            field=models.FloatField(default=0.0),
        ),
    ]
