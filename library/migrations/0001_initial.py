# Generated by Django 3.2 on 2022-05-19 20:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Rack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('uuid', models.UUIDField(default=uuid.UUID('8b8097af-ea82-409a-9682-7326da720b11'))),
                ('status', models.BooleanField(default=True)),
                ('bookshelf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.library')),
            ],
        ),
    ]