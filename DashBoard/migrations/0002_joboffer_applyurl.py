# Generated by Django 4.0.4 on 2022-04-25 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joboffer',
            name='applyurl',
            field=models.URLField(default='https://google.com'),
            preserve_default=False,
        ),
    ]
