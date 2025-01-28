# Generated by Django 5.1.5 on 2025-01-16 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Главное',
                'verbose_name_plural': 'Главное',
            },
        ),
    ]
