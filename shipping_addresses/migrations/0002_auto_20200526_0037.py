# Generated by Django 3.0.5 on 2020-05-26 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_addresses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='exterior_number',
            new_name='external_number',
        ),
    ]
