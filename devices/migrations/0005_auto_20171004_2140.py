# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0004_auto_20171004_0854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oneplus',
            old_name='display',
            new_name='display_size',
        ),
        migrations.RenameField(
            model_name='samsung',
            old_name='display',
            new_name='display_size',
        ),
        migrations.RenameField(
            model_name='xiaomi',
            old_name='display',
            new_name='display_size',
        ),
        migrations.AddField(
            model_name='oneplus',
            name='camera_primary',
            field=models.CharField(default='16MP,f/2.0', max_length=30),
        ),
        migrations.AddField(
            model_name='oneplus',
            name='display_type',
            field=models.CharField(default='AMOLED', max_length=100),
        ),
        migrations.AddField(
            model_name='oneplus',
            name='internal_mem',
            field=models.CharField(default='64GB', max_length=50),
        ),
        migrations.AddField(
            model_name='samsung',
            name='camera_primary',
            field=models.CharField(default='16MP,f/2.0', max_length=30),
        ),
        migrations.AddField(
            model_name='samsung',
            name='display_type',
            field=models.CharField(default='AMOLED', max_length=100),
        ),
        migrations.AddField(
            model_name='samsung',
            name='internal_mem',
            field=models.CharField(default='64GB', max_length=50),
        ),
        migrations.AddField(
            model_name='xiaomi',
            name='camera_primary',
            field=models.CharField(default='16MP,f/2.0', max_length=30),
        ),
        migrations.AddField(
            model_name='xiaomi',
            name='display_type',
            field=models.CharField(default='AMOLED', max_length=100),
        ),
        migrations.AddField(
            model_name='xiaomi',
            name='internal_mem',
            field=models.CharField(default='64GB', max_length=50),
        ),
        migrations.AlterField(
            model_name='oneplus',
            name='battery',
            field=models.CharField(default='3000 mAh', max_length=10),
        ),
        migrations.AlterField(
            model_name='oneplus',
            name='gpu',
            field=models.CharField(default='Adreno', max_length=40),
        ),
        migrations.AlterField(
            model_name='oneplus',
            name='processor',
            field=models.CharField(default='Snapdragon', max_length=200),
        ),
        migrations.AlterField(
            model_name='oneplus',
            name='stockrom',
            field=models.CharField(default='Android', max_length=40),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='battery',
            field=models.CharField(default='3000 mAh', max_length=10),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='gpu',
            field=models.CharField(default='Adreno', max_length=40),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='processor',
            field=models.CharField(default='Snapdragon', max_length=200),
        ),
        migrations.AlterField(
            model_name='samsung',
            name='stockrom',
            field=models.CharField(default='Android', max_length=40),
        ),
        migrations.AlterField(
            model_name='xiaomi',
            name='battery',
            field=models.CharField(default='3000 mAh', max_length=10),
        ),
        migrations.AlterField(
            model_name='xiaomi',
            name='gpu',
            field=models.CharField(default='Adreno', max_length=40),
        ),
        migrations.AlterField(
            model_name='xiaomi',
            name='processor',
            field=models.CharField(default='Snapdragon', max_length=200),
        ),
        migrations.AlterField(
            model_name='xiaomi',
            name='stockrom',
            field=models.CharField(default='Android', max_length=40),
        ),
    ]
