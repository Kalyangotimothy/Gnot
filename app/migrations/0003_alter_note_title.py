# Generated by Django 4.2.4 on 2023-08-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_username_note_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
