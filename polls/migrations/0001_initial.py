# Generated by Django 2.2.1 on 2019-05-17 20:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('forfait_hour', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('firstname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='polls.Roles')),
            ],
        ),
        migrations.CreateModel(
            name='Forfait',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('hour', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Appointement',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True)),
                ('appointement_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Users')),
            ],
        ),
    ]