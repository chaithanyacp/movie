# Generated by Django 3.2.15 on 2022-09-14 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movietable',
            name='img',
            field=models.ImageField(default='null', upload_to='images'),
            preserve_default=False,
        ),
    ]