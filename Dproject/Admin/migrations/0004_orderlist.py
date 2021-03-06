# Generated by Django 2.2.6 on 2020-04-09 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_vehicle_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('unit', models.IntegerField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.Item')),
            ],
        ),
    ]
