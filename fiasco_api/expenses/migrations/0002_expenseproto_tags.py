# Generated by Django 3.1.1 on 2020-09-13 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenseproto',
            name='tags',
            field=models.ManyToManyField(to='tags.Tag'),
        ),
    ]