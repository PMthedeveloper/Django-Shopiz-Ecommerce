# Generated by Django 3.0 on 2019-12-28 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
