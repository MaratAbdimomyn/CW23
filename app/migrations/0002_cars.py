# Generated by Django 4.2.4 on 2023-09-01 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=40)),
                ('models_name', models.CharField(max_length=40)),
                ('engine', models.CharField(max_length=40)),
            ],
        ),
    ]
