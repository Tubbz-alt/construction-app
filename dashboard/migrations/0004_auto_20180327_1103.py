# Generated by Django 2.0.3 on 2018-03-27 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20180326_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='contractor',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]