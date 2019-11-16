from django.contrib.auth.models import User
from django.db import models

RATING_CHOICE = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
)
CATEGORY_CHOICE = (
    ('Phones', 'Телефоны'),
    ('Notebook', 'Ноутбуки'),
    ('Bike', 'Велосипеды')
)


class Product(models.Model):
    name = models.CharField(max_length=25, verbose_name='Название')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICE, verbose_name='Категории')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание')
    picture = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Картинка')

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(User, related_name='users', on_delete=models.CASCADE, verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', related_name='products', on_delete=models.CASCADE, verbose_name='Товар')
    text = models.TextField(max_length=500, verbose_name='Текст отзыва')
    rating = models.CharField(max_length=1, choices=RATING_CHOICE, verbose_name='Оценка')

    def __str__(self):
        return '{} -- {}'.format(self.author, self.product)

