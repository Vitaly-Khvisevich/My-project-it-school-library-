# Generated by Django 3.1.1 on 2020-10-21 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0003_auto_20201014_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='release_year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='comments',
            name='book_id',
            field=models.IntegerField(),
        ),
    ]
