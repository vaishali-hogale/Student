# Generated by Django 5.1.3 on 2024-12-03 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_staff_notification_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_notification',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
