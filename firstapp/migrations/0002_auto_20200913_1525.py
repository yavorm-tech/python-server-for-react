# Generated by Django 3.1.1 on 2020-09-13 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='credential',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='credential',
            name='url',
            field=models.CharField(default='', max_length=255),
        ),
    ]