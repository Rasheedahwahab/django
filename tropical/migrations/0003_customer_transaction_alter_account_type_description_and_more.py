# Generated by Django 4.2.5 on 2023-11-07 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tropical', '0002_remove_account_acc_type_remove_account_branch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=30)),
                ('birth_dates', models.DateField()),
                ('address', models.CharField(max_length=30)),
                ('contact', models.CharField(max_length=20)),
                ('occupation', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_number', models.CharField(max_length=30)),
                ('transaction_date', models.DateField()),
                ('transaction_type', models.CharField(max_length=30)),
                ('transaction_medium', models.CharField(choices=[('C', 'cash'), ('CH', 'cheque'), ('M', 'money')], max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='account_type',
            name='description',
            field=models.TextField(max_length=130),
        ),
        migrations.AlterField(
            model_name='account_type',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
