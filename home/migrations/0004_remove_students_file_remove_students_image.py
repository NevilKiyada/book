# Generated by Django 4.2.11 on 2024-04-12 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_students_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='file',
        ),
        migrations.RemoveField(
            model_name='students',
            name='image',
        ),
    ]
