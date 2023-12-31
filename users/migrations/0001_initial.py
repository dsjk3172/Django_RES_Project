# Generated by Django 4.2.8 on 2023-12-24 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='팀 이름')),
            ],
            options={
                'db_table': 'team',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='이메일')),
                ('username', models.CharField(max_length=128, verbose_name='사용자 이름')),
                ('password', models.CharField(db_column='pw', max_length=255, verbose_name='비밀번호')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.team', verbose_name='소속 팀')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
