# Generated by Django 2.0.3 on 2018-04-30 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0071_auto_20180430_1115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='plan',
            options={'get_latest_by': ['-updated_at'], 'ordering': ['schedule', 'week'], 'permissions': (('admin_plan', 'Administer Plans'),), 'verbose_name': 'Weekly Plan', 'verbose_name_plural': 'Weekly Plans'},
        ),
    ]