# Generated by Django 2.1.2 on 2018-12-21 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0020_auto_20181220_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='mentioned_time',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='post.PointMentionedTime'),
        ),
    ]
