# Generated by Django 5.2.1 on 2025-05-21 17:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='company',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_company_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_company_staff',
        ),
        migrations.AddField(
            model_name='company',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='companies_created', to=settings.AUTH_USER_MODEL),
        ),
    ]
