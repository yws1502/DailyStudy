# Generated by Django 3.2.7 on 2021-09-13 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studygroup',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]