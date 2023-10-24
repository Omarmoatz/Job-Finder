# Generated by Django 4.1.6 on 2023-10-24 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jop',
            name='experince',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='jop',
            name='salary_end',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jop',
            name='salary_start',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jop',
            name='vacancy',
            field=models.PositiveIntegerField(),
        ),
    ]
