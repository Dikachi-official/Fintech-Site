# Generated by Django 4.1.2 on 2023-10-06 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_creditcard_card_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='card_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='cvv',
            field=models.IntegerField(default=439),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='month',
            field=models.CharField(default=10, max_length=200),
        ),
        migrations.AlterField(
            model_name='creditcard',
            name='year',
            field=models.CharField(default=28, max_length=200),
        ),
    ]