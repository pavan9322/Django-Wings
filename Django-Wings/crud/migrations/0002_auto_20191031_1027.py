# Generated by Django 2.2.6 on 2019-10-31 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mobile_number',
            field=models.CharField(max_length=10),
        ),
    ]
