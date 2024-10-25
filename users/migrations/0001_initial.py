# Generated by Django 5.1.1 on 2024-10-25 09:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserConfirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmation_code', models.CharField(max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='confirmation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]