# Generated by Django 2.0.3 on 2018-04-14 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0033_auto_20180414_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='seen_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]