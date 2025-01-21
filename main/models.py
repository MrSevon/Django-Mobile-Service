from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название услуги")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    image = models.ImageField(upload_to='services/', verbose_name="Фото услуги")

    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer_name = models.CharField(max_length=255, verbose_name="Имя клиента")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    additional_info = models.TextField(blank=True, verbose_name="Дополнительная информация")
    items = models.TextField(verbose_name="Товары")
    quantities = models.TextField(verbose_name="Количество каждого товара")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")

    def __str__(self):
        return f"Заказ от {self.customer_name} ({self.created_at})"