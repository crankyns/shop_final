from django.db import models
from django.urls import reverse
from user.models import CustomUser


class Product(models.Model):

    category = models.ForeignKey("Category", verbose_name=("Категория"), on_delete=models.CASCADE)
    subcategory = models.ForeignKey("SubCategory", verbose_name="Подкатегория", null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name="Изображение")
    description = models.TextField(verbose_name="Описание", null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail',  kwargs={"slug_url": self.slug, "slug_category":self.category.slug})



    class Meta():
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Category(models.Model):

    title = models.CharField(max_length=50, verbose_name="Категория")
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug_url": self.slug})


class SubCategory(models.Model):
    
    category = models.ForeignKey(Category,verbose_name="Категория", on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name="Подкатегория")
    slug = models.SlugField(max_length=50, unique=True)
    
    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def get_absolute_url(self):
        return reverse('subcategory',  kwargs={"slug_subcategory":self.slug, "slug_category":self.category.slug})

# class OrderProduct(models.Model):

#     product = models.ForeignKey(Product, verbose_name="Товар к заказу", on_delete=models.CASCADE)
#     quantity = models.PositiveSmallIntegerField(verbose_name="Количество товара")
#     summary_price = models.DecimalField(max_digits=10, verbose_name="Итоговая стоимость продукта")

#     def __str__(self):
#         return self.product

#     class Meta():
#         verbose_name = "Товар к заказу"
#         verbose_name_plural = "Товары к заказу"

    
# class Order(models.Model):

#     products = models.ForeignKey(OrderProduct, verbose_name="Товары в заказе", on_delete=models.CASCADE)
#     owner = models.OneToOneField(CustomUser, verbose_name="Владелец заказа", on_delete=models.CASCADE)
#     city = models.CharField(max_length=30, verbose_name="Город доставки")
#     adress = models.CharField(max_length=70, verbose_name="Адрес доставки")
#     price = models.DecimalField(max_digits=10, verbose_name="Стоимость заказа")

#     def __str_(self):
#         return self.owner, self.products

#     class Meta():
#         verbose_name = "Заказ"
#         verbose_name_plural = "Заказы"