# Generated by Django 3.1.1 on 2020-09-13 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('channels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseProto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('comment', models.TextField(blank=True, null=True)),
                ('amount', models.IntegerField(default=0)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channels.channel')),
                ('kit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.kit')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('expenseproto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='expenses.expenseproto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_fulfilled', models.BooleanField(default=True)),
                ('money_stored', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('expenses.expenseproto', models.Model),
        ),
        migrations.CreateModel(
            name='OngoingExpense',
            fields=[
                ('expenseproto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='expenses.expenseproto')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('scope', models.IntegerField(choices=[(0, 'Month'), (1, 'Year')], default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=('expenses.expenseproto', models.Model),
        ),
    ]