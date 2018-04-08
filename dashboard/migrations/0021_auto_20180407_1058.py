# Generated by Django 2.0.3 on 2018-04-07 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_auto_20180401_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='commencement_date',
            field=models.DateField(blank=True, null=True, verbose_name='Commenecment Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='signing_date',
            field=models.DateField(blank=True, null=True, verbose_name='Agreement Signing Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='site_handover',
            field=models.DateField(blank=True, null=True, verbose_name='Site Handover Date'),
        ),
    ]