# Generated by Django 4.2.8 on 2023-12-24 00:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('content', models.TextField(blank=True, null=True, verbose_name='content')),
                ('is_complete', models.BooleanField(default=False, verbose_name='is_complete')),
                ('completed_date', models.DateTimeField(blank=True, null=True, verbose_name='completed_date')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_at')),
                ('modified_at', models.DateTimeField(blank=True, null=True, verbose_name='modified_at')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='create_user')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.team', verbose_name='team')),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_complete', models.BooleanField(default=False, verbose_name='is_complete')),
                ('completed_date', models.DateTimeField(blank=True, null=True, verbose_name='completed_date')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created_at')),
                ('modified_at', models.DateTimeField(blank=True, null=True, verbose_name='modified_at')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.task', verbose_name='task')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.team', verbose_name='team')),
            ],
            options={
                'db_table': 'subtask',
            },
        ),
    ]