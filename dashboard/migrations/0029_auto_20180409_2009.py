# Generated by Django 2.0.3 on 2018-04-09 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0028_auto_20180408_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='projects_followed',
            field=models.ManyToManyField(blank=True, related_name='project_followers', to='dashboard.Project'),
        ),
    ]