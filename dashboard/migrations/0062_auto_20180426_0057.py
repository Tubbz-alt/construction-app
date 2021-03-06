# Generated by Django 2.0.3 on 2018-04-25 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0061_remove_notification_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='created_by',
        ),
        migrations.AddField(
            model_name='notification',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='all_notifications', to='dashboard.Project'),
            preserve_default=False,
        ),
    ]
