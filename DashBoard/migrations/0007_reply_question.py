# Generated by Django 4.0.4 on 2022-05-03 20:52

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('DashBoard', '0006_reply_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.expressions.Case, to='DashBoard.question'),
            preserve_default=False,
        ),
    ]
