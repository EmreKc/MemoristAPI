# Generated by Django 2.1.2 on 2019-01-01 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0025_auto_20190101_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointmentionedtime',
            name='date_type',
            field=models.IntegerField(blank=True, choices=[(0, 'single'), (1, 'period')], null=True),
        ),
    ]
