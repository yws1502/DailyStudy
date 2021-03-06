# Generated by Django 3.2.7 on 2021-09-12 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['is_read', '-created']},
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='group_reader',
            new_name='group_leader',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='group_id',
        ),
        migrations.AddField(
            model_name='message',
            name='is_invite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='has_group',
            field=models.BooleanField(default=False),
        ),
    ]
