# Generated by Django 2.2.1 on 2019-05-17 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('law', '0004_auto_20190517_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conviction',
            name='criminal_case_number',
            field=models.CharField(max_length=200, null=True, verbose_name='Номер уголовного дело'),
        ),
    ]
