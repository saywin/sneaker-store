from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва категорії")
    image = models.ImageField(
        upload_to="categories/",
        null=True,
        blank=True,
        verbose_name="Зображення",
    )
    slug = models.SlugField(unique=True, null=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name="subcategories",
        verbose_name="Категорія",
    )

    def get_absolute_url(self):
        pass

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Категорія: pk = {self.pk}, title = {self.title}"

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва товару")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Ціна")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    watched = models.PositiveIntegerField(default=0, verbose_name="Перегляди")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Кількість на складі")
    description = models.TextField(default="Тут скоро з'явиться опис товару", verbose_name="Опис товару")
    info = models.TextField(default="Додаткова інформація про товар", verbose_name="Інформація о товарі")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Категорія")
    slug = models.SlugField(unique=True, null=True)
    size = models.IntegerField(default=37, verbose_name="Розмір")
    color = models.CharField(max_length=100, default="gold", verbose_name="Колір/Матеріал")

    def get_absolute_url(self):
        pass

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"Товар: pk={self.pk}, title={self.title}, price={self.price}, quantity={self.quantity}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товари"


class Gallery(models.Model):
    image = models.ImageField(upload_to="products/", verbose_name="Зображення")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images", verbose_name="Товар")

    class Meta:
        verbose_name = "Зображення"
        verbose_name_plural = "Галерея товарів"
