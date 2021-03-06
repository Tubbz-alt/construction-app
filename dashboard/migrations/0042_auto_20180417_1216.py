# Generated by Django 2.0.3 on 2018-04-17 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0041_auto_20180416_0158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='Construction Activity')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['title', 'updated_at'],
                'verbose_name': 'Construction Activity',
                'verbose_name_plural': 'Construction Activities',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_start_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Planned Amount')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('activities', models.ManyToManyField(null=True, related_name='activity_plans', to='dashboard.Activity', verbose_name='Planned Activities')),
            ],
            options={
                'ordering': ['schedule', 'period_start_date'],
                'permissions': (('admin_plan', 'Administer Plans'),),
                'verbose_name_plural': 'Schedule Plans',
                'verbose_name': 'Schedule Plan',
                'get_latest_by': ['-period_start_date', '-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='Executed Amount')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description of executed works')),
                ('slippage_reason', models.TextField(blank=True, null=True, verbose_name='Reasons and descrioption of slippage')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='Additional Notes and Remarks')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('activities', models.ManyToManyField(null=True, related_name='activity_reports', to='dashboard.Activity', verbose_name='Executed Activities')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='dashboard.Plan')),
            ],
            options={
                'ordering': ['plan', '-updated_at'],
                'permissions': (('admin_report', 'Administer Report'),),
                'get_latest_by': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Schedule Title')),
                ('description', models.TextField(blank=True, null=True)),
                ('period', models.CharField(choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')], max_length=30, verbose_name='Scheduled Period')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active Status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='dashboard.Project')),
            ],
            options={
                'ordering': ['is_active', 'project', '-updated_at'],
                'permissions': (('admin_schedule', 'Administer Schedule'),),
                'get_latest_by': ['updated_at'],
            },
        ),
        migrations.AddField(
            model_name='plan',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plans', to='dashboard.Schedule'),
        ),
    ]
