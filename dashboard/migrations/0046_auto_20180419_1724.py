# Generated by Django 2.0.3 on 2018-04-19 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0045_project_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='body',
            field=models.TextField(),
        ),
    ]
