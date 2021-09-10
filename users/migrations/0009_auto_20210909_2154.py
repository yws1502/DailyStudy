# Generated by Django 3.2.7 on 2021-09-09 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_algorithm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='algorithm',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='algorithm',
            name='type',
            field=models.CharField(choices=[('IMP', 'Implementation'), ('GRE', 'Greedy'), ('STR', 'String'), ('DS', 'Structures'), ('GRA', 'Graphs'), ('DP', 'DynamicProgramming'), ('MA', 'Math'), ('BRU', 'Bruteforce')], max_length=3),
        ),
    ]