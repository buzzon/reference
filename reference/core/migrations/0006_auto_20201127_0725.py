# Generated by Django 3.1.3 on 2020-11-27 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201127_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
