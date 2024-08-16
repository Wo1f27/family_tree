# Generated by Django 5.0.6 on 2024-08-15 07:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('patronymic', models.CharField(blank=True, max_length=50)),
                ('date_of_birth', models.DateTimeField(blank=True)),
                ('date_of_death', models.DateTimeField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('profile_avatar', models.ImageField(upload_to='profile/')),
                ('deleted', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'People',
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=256)),
                ('is_primary', models.BooleanField(default=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='person_card.person')),
            ],
            options={
                'db_table': 'emails',
                'unique_together': {('person', 'email')},
            },
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('is_primary', models.BooleanField(default=False)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='person_card.person')),
            ],
            options={
                'db_table': 'phone_numbers',
                'unique_together': {('person', 'phone_number')},
            },
        ),
    ]
