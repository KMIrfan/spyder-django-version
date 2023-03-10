# Generated by Django 4.1.5 on 2023-01-17 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_alter_seller_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cust',
            name='dist',
            field=models.CharField(default='malappuram', max_length=40),
        ),
        migrations.AddField(
            model_name='cust',
            name='house',
            field=models.CharField(default='select', max_length=40),
        ),
        migrations.AddField(
            model_name='cust',
            name='landmark',
            field=models.CharField(default='select', max_length=40),
        ),
        migrations.AddField(
            model_name='cust',
            name='pin',
            field=models.BigIntegerField(default=671631),
        ),
        migrations.AddField(
            model_name='cust',
            name='post',
            field=models.CharField(default='select', max_length=40),
        ),
        migrations.AddField(
            model_name='cust',
            name='state',
            field=models.CharField(default='kerala', max_length=40),
        ),
    ]
