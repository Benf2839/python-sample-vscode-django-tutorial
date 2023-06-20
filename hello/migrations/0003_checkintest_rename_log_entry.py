# Generated by Django 4.1.7 on 2023-06-15 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckinTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('alumni', models.BooleanField(default=False)),
                ('release_info', models.BooleanField(default=False)),
                ('id_number', models.IntegerField()),
                ('checked_in', models.BooleanField(default=False)),
                ('checked_in_time', models.DateTimeField(blank=True, null=True)),
                ('table_number', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Checkin_test',
            },
        ),
        migrations.RenameModel(
            old_name='Log',
            new_name='Entry',
        ),
    ]