from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Category, Product


class Index(ListView):
    """Головна сторінка"""

    model = Product
    context_object_name = "categories"
    extra_context = {"title": "Головна сторінка"}
    template_name = "shop/index.html"

    def get_queryset(self):
        categories = Category.objects.filter(parent=None)
        return categories


class SubCategories(ListView):
    """Вивід підкатегорій на окремій сторінці"""

    model = Product
    context_object_name = "products"
    template_name = "shop/category_page.html"

    def get_queryset(self):
        """Отримання всіх товарів певної категорії, включаючи вкладені підкатегорії"""
        parent_category = Category.objects.prefetch_related(
            "subcategories"
        ).get(slug=self.kwargs["slug"])
        all_subcategories = parent_category.get_all_subcategories()
        all_subcategories.append(parent_category)
        products = Product.objects.filter(
            category__in=all_subcategories
        ).order_by("?")
        return products
