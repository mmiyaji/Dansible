# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-17 01:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=100)),
                ('comment', models.TextField(default='')),
                ('config_type', models.CharField(choices=[('f', 'File'), ('d', 'Data'), ('c', 'Command')], db_index=True, default='c', max_length=10)),
                ('isvalid', models.BooleanField(db_index=True, default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConfigCommand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=100)),
                ('comment', models.TextField(default='')),
                ('command', models.CharField(db_index=True, default='', max_length=100)),
                ('command_user', models.CharField(db_index=True, default='', max_length=100)),
                ('isvalid', models.BooleanField(db_index=True, default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConfigData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=100)),
                ('comment', models.TextField(default='')),
                ('file_path', models.CharField(db_index=True, default='', max_length=100)),
                ('file_permittion', models.CharField(db_index=True, default='', max_length=100)),
                ('file_owner', models.CharField(db_index=True, default='', max_length=100)),
                ('file_group', models.CharField(db_index=True, default='', max_length=100)),
                ('isvalid', models.BooleanField(db_index=True, default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConfigFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=100)),
                ('comment', models.TextField(default='')),
                ('file_path', models.CharField(db_index=True, default='', max_length=100)),
                ('file_permittion', models.CharField(db_index=True, default='', max_length=100)),
                ('file_owner', models.CharField(db_index=True, default='', max_length=100)),
                ('file_group', models.CharField(db_index=True, default='', max_length=100)),
                ('isvalid', models.BooleanField(db_index=True, default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='OSTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=100)),
                ('comment', models.TextField(default='')),
                ('isvalid', models.BooleanField(db_index=True, default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=100)),
                ('comment', models.TextField(default='')),
                ('isvalid', models.BooleanField(db_index=True, default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServerAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=100)),
                ('comment', models.TextField(default='')),
                ('isvalid', models.BooleanField(db_index=True, default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.AddField(
            model_name='ostemplate',
            name='server_attribute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ServerAttribute'),
        ),
        migrations.AddField(
            model_name='config',
            name='config_command',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ConfigCommand'),
        ),
        migrations.AddField(
            model_name='config',
            name='config_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ConfigData'),
        ),
        migrations.AddField(
            model_name='config',
            name='config_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ConfigFile'),
        ),
    ]
