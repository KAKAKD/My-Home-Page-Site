# Generated by Django 3.0.8 on 2020-07-15 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workpost',
            name='git_url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='workpost',
            name='page_url',
            field=models.URLField(null=True),
        ),
    ]