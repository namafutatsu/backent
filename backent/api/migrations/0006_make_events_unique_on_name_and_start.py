# Generated by Django 2.0.2 on 2018-02-20 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backent_api', '0005_remove_event_end'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={},
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together={('name', 'start')},
        ),
    ]
