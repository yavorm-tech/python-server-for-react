# Generated by Django 3.1.1 on 2020-09-16 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200916_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
