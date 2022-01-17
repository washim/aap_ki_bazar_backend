# Generated by Django 3.2.11 on 2022-01-15 16:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='', max_length=30)),
                ('mobile', models.CharField(max_length=11)),
                ('address', models.CharField(default='', max_length=255)),
                ('ward_no', models.CharField(default='', max_length=50)),
                ('pincode', models.CharField(default='', max_length=10)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.AddField(
            model_name='invoice',
            name='shipping',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='billing.shipping'),
            preserve_default=False,
        ),
    ]
