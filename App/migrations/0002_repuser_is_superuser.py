# Generated by Django 3.2.7 on 2021-09-19 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
