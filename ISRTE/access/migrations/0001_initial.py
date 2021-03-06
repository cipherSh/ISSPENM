# Generated by Django 2.2.1 on 2019-05-12 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20190511_1702'),
        ('auth', '0011_update_proxy_permissions'),
        ('persons', '0002_auto_20190512_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('special', models.BooleanField(default=False, verbose_name='Специальный допуск')),
                ('doc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Criminals', verbose_name='Досье')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Персональный доступ',
                'verbose_name_plural': 'Персональный доступ',
            },
        ),
        migrations.CreateModel(
            name='GroupAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Criminals', verbose_name='Досье')),
                ('group_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Групповой доступ',
                'verbose_name_plural': 'Групповой доступ',
            },
        ),
    ]
