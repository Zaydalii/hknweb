# Generated by Django 2.1.5 on 2019-02-17 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0007_offchallenge_request_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='offchallenge',
            name='officer_comment',
            field=models.TextField(blank=True, default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='offchallenge',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
    ]