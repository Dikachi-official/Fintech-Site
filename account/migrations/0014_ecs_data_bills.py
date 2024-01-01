# Generated by Django 4.1.2 on 2023-10-06 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0013_kyc_id_select'),
    ]

    operations = [
        migrations.CreateModel(
            name='ECS_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecs_id', shortuuid.django_fields.ShortUUIDField(alphabet='123456789', length=16, max_length=16, prefix='', unique=True)),
                ('payer', models.CharField(max_length=300)),
                ('upper_Limit', models.FloatField()),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ecs_account', to='account.account')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ecs_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('completed', models.BooleanField(default=False)),
                ('bill_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.ecs_data')),
            ],
        ),
    ]