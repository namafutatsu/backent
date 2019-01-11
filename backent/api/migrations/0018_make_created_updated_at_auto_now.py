# Generated by Django 2.1.3 on 2019-01-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backent_api', '0017_add_created_updated_at_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]