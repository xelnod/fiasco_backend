# Generated by Django 2.2.7 on 2019-11-30 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='preferred_class',
        ),
        migrations.AddField(
            model_name='user',
            name='income',
            field=models.IntegerField(default=50000),
        ),
    ]
