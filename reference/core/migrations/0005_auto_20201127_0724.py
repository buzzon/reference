# Generated by Django 3.1.3 on 2020-11-27 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_board_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='slug',
            field=models.SlugField(default='ERROR-slug', max_length=255),
        ),
    ]
