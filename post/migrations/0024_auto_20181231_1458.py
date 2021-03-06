# Generated by Django 2.1.2 on 2018-12-31 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0023_auto_20181231_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_type', models.IntegerField(choices=[(0, 'seperate'), (1, 'path')])),
                ('location_list', models.ManyToManyField(blank=True, to='post.PointLocation')),
            ],
        ),
        migrations.RemoveField(
            model_name='pathlocation',
            name='location_from',
        ),
        migrations.RemoveField(
            model_name='pathlocation',
            name='location_to',
        ),
        migrations.RemoveField(
            model_name='memory',
            name='pathlocations',
        ),
        migrations.RemoveField(
            model_name='memory',
            name='pointlocations',
        ),
        migrations.DeleteModel(
            name='PathLocation',
        ),
        migrations.AddField(
            model_name='memory',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='post.Location'),
        ),
    ]
