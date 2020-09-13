# Generated by Django 3.1.1 on 2020-09-13 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_tag_owner'),
        ('categories', '0002_auto_20200913_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='cat',
            name='tags',
            field=models.ManyToManyField(blank=True, to='tags.Tag'),
        ),
    ]