# Generated by Django 2.0.3 on 2018-04-23 19:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0053_notification_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='project',
        ),
    ]
