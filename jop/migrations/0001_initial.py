# Generated by Django 4.1.6 on 2023-10-24 00:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('logo', models.ImageField(upload_to='company')),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Jop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('location', django_countries.fields.CountryField(max_length=2)),
                ('salary_start', models.IntegerField(blank=True, null=True)),
                ('salary_end', models.IntegerField(blank=True, null=True)),
                ('cratesd_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('vacancy', models.IntegerField()),
                ('experince', models.IntegerField()),
                ('jop_nature', models.CharField(choices=[('FullTime', 'Full_Time'), ('PartTime', 'PartTime'), ('Remote', 'Remote'), ('Freelance', 'Freelance')], max_length=10)),
                ('description', models.TextField(max_length=5000)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='jop_category', to='jop.category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jop_company', to='jop.company')),
            ],
        ),
    ]