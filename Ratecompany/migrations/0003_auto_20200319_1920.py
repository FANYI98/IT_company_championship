# Generated by Django 3.0.2 on 2020-03-19 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ratecompany', '0002_auto_20200319_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='Ratecompany.Company'),
        ),
    ]
