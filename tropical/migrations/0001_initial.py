# Generated by Django 4.2.5 on 2023-10-03 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('description', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('manager', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=30)),
                ('opening_date', models.DateField()),
                ('account_balance', models.IntegerField()),
                ('status', models.CharField(choices=[('A', 'active'), ('IN', 'inactive')], max_length=10)),
                ('acc_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tropical.account_type')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tropical.branch')),
            ],
        ),
    ]
