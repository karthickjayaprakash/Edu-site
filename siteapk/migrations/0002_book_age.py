# Generated by Django 3.1.2 on 2021-08-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='age',
            field=models.IntegerField(default=18, max_length=3),
        ),
    ]
