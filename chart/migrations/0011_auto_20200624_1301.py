# Generated by Django 3.0.3 on 2020-06-24 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0010_auto_20200622_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmed',
            name='Date',
            field=models.DateField(),
        ),
    ]