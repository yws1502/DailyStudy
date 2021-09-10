# Generated by Django 3.2.7 on 2021-09-09 12:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_delete_algorithm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('language', models.CharField(choices=[('PYT', 'Python3'), ('PYP', 'PyPy3'), ('JA', 'Java11'), ('C', 'C99'), ('C+', 'C++17'), ('JS', 'Js'), ('GO', 'GO'), ('RU', 'Ruby')], max_length=3)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('link', models.URLField()),
                ('type', models.CharField(choices=[('IMP', 'Implementation'), ('GRE', 'Greedy'), ('STR', 'String'), ('DS', 'DataStructures'), ('GRA', 'Graphs'), ('DP', 'DynamicProgramming'), ('MA', 'Math'), ('BRU', 'Bruteforce')], max_length=3)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('profile_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
            ],
        ),
    ]