# Generated by Django 2.2.1 on 2019-07-29 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ck_editor', '0002_auto_20190729_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
