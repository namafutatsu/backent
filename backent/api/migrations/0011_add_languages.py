# Generated by Django 2.1.3 on 2019-01-03 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backent_api', '0010_populate_event_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(choices=[('de', 'German'), ('en', 'English'), ('es', 'Spanish'), ('fr', 'French'), ('it', 'Italian'), ('ru', 'Russian')], max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='languages_spoken',
            field=models.ManyToManyField(blank=True, null=True, related_name='events', to='backent_api.Language'),
        ),
    ]
