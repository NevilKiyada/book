# Generated by Django 4.2.11 on 2024-04-21 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_discussion',
            new_name='book_description',
        ),
    ]