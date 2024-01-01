# Generated by Django 4.1.2 on 2023-10-09 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_creditcard_card_status_alter_creditcard_cvv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transfer_type',
            field=models.CharField(choices=[('transfer', 'Transfer'), ('deposit', 'Deposit'), ('withdrawal', 'Withdrawal')], max_length=10),
        ),
    ]