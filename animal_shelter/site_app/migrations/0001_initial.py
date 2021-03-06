# Generated by Django 3.1.1 on 2020-09-07 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('review', models.TextField(verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50, verbose_name='Кличка')),
                ('breed', models.CharField(max_length=50, verbose_name='Порода')),
                ('description', models.TextField(verbose_name='Описание')),
                ('receipt_date', models.DateField(auto_now=True, verbose_name='Дата поступления')),
                ('kind_of', models.CharField(choices=[('Собака', 'Собака'), ('Кошка', 'Кошка'), ('Птица', 'Птица')], max_length=10, verbose_name='Вид')),
                ('foto', models.ImageField(upload_to='', verbose_name='Фото')),
                ('recalls', models.ManyToManyField(related_name='pet_recalls', to='site_app.Recall', verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'Питомец',
                'verbose_name_plural': 'Питомцы',
            },
        ),
    ]
