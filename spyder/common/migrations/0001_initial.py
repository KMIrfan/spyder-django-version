# Generated by Django 4.1.5 on 2023-01-06 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cust',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_fname', models.CharField(max_length=20)),
                ('cust_lname', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('cust_email', models.CharField(max_length=20)),
                ('cust_pass', models.CharField(max_length=40)),
                ('cust_cnfrmpass', models.CharField(max_length=40)),
            ],
        ),
    ]