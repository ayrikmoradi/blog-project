# Generated by Django 5.1.3 on 2024-11-18 01:51

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('checking', 'checking'), ('rejected', 'rejected'), ('published', 'published')], default='checking', max_length=15)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Articles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
