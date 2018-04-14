# Generated by Django 2.0.3 on 2018-04-14 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0036_remove_project_completion_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'get_latest_by': 'updated_at', 'ordering': ['status', '-updated_at', 'short_name'], 'permissions': (('admin_project', 'Administer Project'),)},
        ),
    ]
