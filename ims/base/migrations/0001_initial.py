# Generated by Django 5.0.3 on 2024-03-20 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
