# Generated by Django 2.2.1 on 2019-07-29 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ck_editor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]