# Generated by Django 3.0.3 on 2020-06-16 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0002_auto_populate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confirmed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=100)),
                ('France', models.FloatField(null=True)),
                ('Germany', models.FloatField(null=True)),
                ('Korea_South', models.FloatField(null=True)),
                ('US', models.FloatField(null=True)),
                ('United_Kingdom', models.FloatField(null=True)),
            ],
        ),
    ]
