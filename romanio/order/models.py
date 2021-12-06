from django.db import models
from mainapp.models import Product
from user.models import CustomUser




class Order(models.Model):
    user = models.ForeignKey(CustomUser,related_name='user', verbose_name='Пользователь', on_delete=models.CASCADE)
    address = models.CharField(max_length=100, verbose_name='Адрес доставки')
    city = models.CharField(max_length=30, verbose_name='Город')
    postal_code = models.CharField(max_length=20, verbose_name='Почтовый индекс')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    paid = models.BooleanField(default=False, verbose_name='Оплачено')
    
    class Meta:
        ordering = ("-created",)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


