# Generated by Django 4.2.4 on 2023-08-29 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='second_name',
            new_name='surname',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='user'),
        ),
    ]
