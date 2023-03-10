# Generated by Django 4.1.7 on 2023-02-25 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='название')),
                ('mail', models.EmailField(max_length=200, verbose_name='почта')),
                ('text', models.TextField(max_length=3000, verbose_name='описание')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='дата создание')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('status', models.CharField(choices=[('active', 'Активно'), ('blocked', 'Заблокировано')], default='active', max_length=10)),
            ],
        ),
    ]
