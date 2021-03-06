# Generated by Django 2.2 on 2019-11-16 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Название')),
                ('category', models.CharField(choices=[('Phones', 'Телефоны'), ('Notebook', 'Ноутбуки'), ('Bike', 'Велосипеды')], max_length=20, verbose_name='Категории')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='user_pics', verbose_name='Картинка')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='Текст отзыва')),
                ('rating', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], verbose_name='Оценка')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='webapp.Product', verbose_name='Товар')),
            ],
        ),
    ]
