# Generated by Django 3.2.7 on 2021-09-08 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210909_0221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='social_website',
        ),
    ]