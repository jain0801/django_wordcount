# Generated by Django 3.1 on 2020-08-10 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='wordcount',
            field=models.TextField(),
        ),
    ]
