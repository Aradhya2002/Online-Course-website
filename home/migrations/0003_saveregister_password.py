# Generated by Django 3.0.5 on 2022-11-06 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20221106_2125'),
    ]

    operations = [
        migrations.AddField(
            model_name='saveregister',
            name='password',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
    ]