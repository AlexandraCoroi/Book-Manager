# Generated by Django 5.0.2 on 2024-02-28 06:49

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default='7078ac497ece75427ef0dff28242f308aa1794f9dba1a8e4d6cf599a3d81bea3', max_length=64, null=True)),
                ('expires_at', models.DateTimeField(default=datetime.datetime(2024, 2, 28, 6, 59, 11, 503614, tzinfo=datetime.timezone.utc))),
                ('activated_at', models.DateTimeField(default=None, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='activation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
