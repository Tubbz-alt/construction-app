# Generated by Django 2.0.3 on 2018-04-17 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0043_auto_20180417_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(choices=[('advance', 'Advance Payment'), ('interim', 'Interim Payment'), ('final', 'Final Payment')], default='interim', max_length=60)),
                ('status', models.IntegerField(verbose_name='Payment status')),
                ('title', models.CharField(max_length=100, verbose_name='Payment title')),
                ('service_sum', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('material_onsite', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('advance_repayment', models.DecimalField(decimal_places=2, default=30.0, max_digits=5, verbose_name='Advance repayment(%)')),
                ('retention_repayment', models.DecimalField(decimal_places=2, default=5.0, max_digits=5, verbose_name='Retention repayment(%)')),
                ('penality_repayment', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Penality repayment(%)')),
                ('prepared_by', models.CharField(blank=True, max_length=100, null=True)),
                ('submitted_ref_no', models.CharField(blank=True, max_length=30, null=True, verbose_name='Submittal Letter Ref. No.')),
                ('submitted_date', models.DateField(blank=True, null=True, verbose_name='Approval/Rejection date')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('previous_payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_payment', to='dashboard.Payment')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='dashboard.Project')),
            ],
            options={
                'permissions': (('admin_payment', 'Administer Payment'),),
                'ordering': ['project', 'previous_payment'],
                'get_latest_by': ['-updated_at'],
            },
        ),
    ]