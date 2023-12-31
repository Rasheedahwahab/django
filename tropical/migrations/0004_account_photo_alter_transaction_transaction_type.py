# Generated by Django 4.2.5 on 2023-11-08 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tropical', '0003_customer_transaction_alter_account_type_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='photo',
            field=models.ImageField(default=0, upload_to='photos'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('D', 'deposit'), ('W', 'withdraw')], max_length=10),
        ),
    ]
