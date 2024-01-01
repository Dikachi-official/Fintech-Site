# Generated by Django 4.1.2 on 2023-10-05 12:47

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_kyc_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='pin_number',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='123456789', length=3, max_length=4, prefix='1', unique=True),
        ),
    ]