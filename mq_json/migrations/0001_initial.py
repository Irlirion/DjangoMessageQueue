# Generated by Django 3.1.1 on 2020-09-24 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('messages', models.TextField()),
            ],
        ),
    ]
