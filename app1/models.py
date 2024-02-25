from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    title = models.CharField(max_length=30)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Category,s')
        ordering = ['title']

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    about = models.TextField(max_length=800, default='ویژگی محصولات')
    price = models.DecimalField(max_digits=12, decimal_places=0)
    is_discount = models.BooleanField(default=False)
    discount = models.DecimalField(max_digits=12, decimal_places=0, blank=True, null=True)
    at_creat = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)], default=0)
    time_update = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['name']


class Image(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')


class Costumer(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    location = models.CharField(max_length=500)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}-{self.last_name}'

    class Meta:
        verbose_name = _('Costumer')
        verbose_name_plural = _('Costumers')
        ordering = ['name']



