# Generated by Django 3.0.5 on 2021-04-02 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tea',
            name='description',
            field=models.TextField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tea',
            name='origin',
            field=models.CharField(max_length=30),
        ),
    ]
