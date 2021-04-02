# Generated by Django 3.0.5 on 2021-04-02 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210402_0309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='feeding date')),
                ('drink', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('S', 'Snack'), ('D', 'Dinner')], default='B', max_length=1)),
                ('tea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Tea')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
