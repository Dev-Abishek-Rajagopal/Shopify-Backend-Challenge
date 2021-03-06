# Generated by Django 3.2.7 on 2021-09-21 00:10

import App.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20210919_0245'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImgRep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default=App.models.default_rep, upload_to=App.models.upload_to, verbose_name='Image File')),
                ('name', models.CharField(default=App.models.default_to, max_length=150)),
                ('scope', models.CharField(choices=[('PUBLIC', 'public'), ('PRIVATE', 'PRIVATE')], default='PUBLIC', max_length=20)),
                ('access', models.CharField(choices=[('READONLY', 'readonly'), ('FULLACCESS', 'FULL')], default='READONLY', max_length=20)),
                ('price', models.DecimalField(decimal_places=2, default=2.0, max_digits=10)),
                ('discount', models.IntegerField(default=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Rep_User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ImgCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('img', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cart_Img', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cart_User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
