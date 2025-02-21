# Generated by Django 4.2 on 2025-01-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default='Unknown Director', max_length=100),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='movie',
            name='synopsis',
            field=models.TextField(default='No synopsis available'),
        ),
    ]
