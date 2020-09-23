# Generated by Django 3.1.1 on 2020-09-16 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='credentials',
            name='password',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='credentials',
            name='username',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddConstraint(
            model_name='credentials',
            constraint=models.UniqueConstraint(fields=('username', 'url'), name='unique_fields'),
        ),
    ]
