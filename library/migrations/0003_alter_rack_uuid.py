# Generated by Django 3.2 on 2022-05-25 16:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20220519_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('41e98ace-efd6-42e9-baff-13847217163a')),
        ),
    ]