# Generated by Django 4.2.6 on 2023-10-11 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('code', models.PositiveIntegerField(blank=True, null=True, unique=True)),
                ('logo', models.ImageField(blank=True, upload_to='images/')),
                ('capital', models.CharField(blank=True, max_length=200)),
                ('population', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'counties',
            },
        ),
        migrations.CreateModel(
            name='Subcounty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('population', models.PositiveIntegerField()),
                ('county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_counties', to='api.county')),
            ],
            options={
                'verbose_name_plural': 'subcounties',
            },
        ),
    ]
