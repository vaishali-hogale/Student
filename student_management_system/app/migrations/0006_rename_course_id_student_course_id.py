# Generated by Django 5.1.3 on 2024-11-24 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_courseid_student_course_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='course_Id',
            new_name='course_id',
        ),
    ]
