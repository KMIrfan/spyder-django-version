# Generated by Django 4.1.5 on 2023-01-06 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0006_alter_seller_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='seller_usr',
            field=models.IntegerField(default=0),
        ),
    ]
