# Generated by Django 5.0.3 on 2024-03-14 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_book_options_alter_genre_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='views',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
