# Generated by Django 4.2.10 on 2024-04-01 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seance',
            name='is_free',
            field=models.BooleanField(default=True),
        ),
    ]