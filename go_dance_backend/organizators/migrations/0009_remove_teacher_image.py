# Generated by Django 4.2.10 on 2024-05-12 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizators', '0008_company_teachers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='image',
        ),
    ]
