# Generated by Django 4.2.11 on 2024-04-11 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_students_addresh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
