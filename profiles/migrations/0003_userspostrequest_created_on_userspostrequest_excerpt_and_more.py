# Generated by Django 4.2.11 on 2024-03-05 16:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userspostrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='userspostrequest',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userspostrequest',
            name='excerpt',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='userspostrequest',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
