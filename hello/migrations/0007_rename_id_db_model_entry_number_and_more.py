# Generated by Django 4.1.7 on 2023-06-20 17:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_db_model_delete_checkintest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='db_model',
            old_name='id',
            new_name='entry_number',
        ),
        migrations.AlterField(
            model_name='db_model',
            name='checked_in_time',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
