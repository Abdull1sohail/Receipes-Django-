# Generated by Django 4.1.7 on 2023-09-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0003_rename_user_receipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='receipe_view_count',
            field=models.IntegerField(default=1),
        ),
    ]
