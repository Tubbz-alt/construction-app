# Generated by Django 2.0.3 on 2018-04-23 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('dashboard', '0049_auto_20180421_1429'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'get_latest_by': ['-updated_at'], 'ordering': ['-updated_at']},
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='title',
            new_name='subject',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_claim_admin',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_insurance_admin',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_payment_admin',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_project_admin',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_variation_admin',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='body',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='notification_type',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='project',
        ),
        migrations.AddField(
            model_name='notification',
            name='content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='message',
            field=models.TextField(default='Default message', verbose_name='Notification message'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
