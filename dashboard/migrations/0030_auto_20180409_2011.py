# Generated by Django 2.0.3 on 2018-04-09 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0029_auto_20180409_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='projects_administered',
            field=models.ManyToManyField(blank=True, related_name='projects_admins', to='dashboard.Project'),
        ),
    ]