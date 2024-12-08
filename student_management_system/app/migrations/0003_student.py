# Generated by Django 5.1.3 on 2024-11-23 04:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_course_alter_customuser_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=100)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('courseId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.course')),
            ],
        ),
    ]
