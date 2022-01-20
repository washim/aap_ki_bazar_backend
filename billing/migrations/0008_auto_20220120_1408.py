# Generated by Django 3.2.11 on 2022-01-20 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0007_alter_invoice_shipping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invoice', to='billing.invoice'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='billing.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight_attributes',
            field=models.CharField(choices=[('Kg', 'Kg'), ('Piece', 'Piece')], default='Kg', max_length=10),
        ),
    ]
