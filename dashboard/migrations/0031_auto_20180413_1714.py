# Generated by Django 2.0.3 on 2018-04-13 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0030_auto_20180409_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernotification',
            name='notification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notifications', to='dashboard.Notification'),
        ),
    ]