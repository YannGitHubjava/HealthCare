# Generated by Django 3.0.1 on 2019-12-28 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firtName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
            ],
        ),
    ]
