# Generated by Django 3.2.7 on 2021-09-22 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_imgrep_color_palette'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgcart',
            name='img',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cart_Img', to='App.imgrep'),
        ),
    ]
