# Generated by Django 3.2.7 on 2021-09-13 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study_groups', '0001_initial'),
        ('users', '0015_auto_20210912_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='has_group',
        ),
        migrations.AddField(
            model_name='profile',
            name='group_id',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='study_groups.studygroup'),
        ),
    ]
