# Generated by Django 2.1.2 on 2018-10-27 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_registereduser_activeemail_status'),
        ('post', '0002_memory_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='memory',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='login.RegisteredUser'),
            preserve_default=False,
        ),
    ]
