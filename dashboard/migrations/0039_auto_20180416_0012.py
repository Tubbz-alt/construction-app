# Generated by Django 2.0.3 on 2018-04-15 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0038_auto_20180415_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_seen', models.BooleanField(default=False, verbose_name='Seen')),
                ('seen_date', models.DateTimeField(blank=True, null=True)),
                ('is_email_sent', models.BooleanField(default=False, verbose_name='Email Sent Status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['is_seen', 'notification'],
                'get_latest_by': ['seen_date'],
            },
        ),
        migrations.RemoveField(
            model_name='notification',
            name='is_email_sent',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='is_seen',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='notification_url',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='notify_to',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='seen_date',
        ),
        migrations.AddField(
            model_name='usernotification',
            name='notification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notifications', to='dashboard.Notification'),
        ),
        migrations.AddField(
            model_name='usernotification',
            name='notify_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_notifications', to=settings.AUTH_USER_MODEL),
        ),
    ]
