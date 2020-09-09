# Generated by Django 3.1.1 on 2020-09-09 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0009_auto_20200909_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='comment',
        ),
        migrations.AddField(
            model_name='pet',
            name='comment',
            field=models.ManyToManyField(blank=True, to='site_app.Comment', verbose_name='Комментарий'),
        ),
    ]
