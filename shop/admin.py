from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product, Gallery


admin.site.register(Gallery)


class GalleryInline(admin.TabularInline):
    pk_name = "product"
    model = Gallery
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "parent", "get_category_count"]
    prepopulated_fields = {"slug": ("title",)}

    def get_category_count(self, obj):
        if obj.products:
            return len(obj.products.all())
        return "0"

    get_category_count.short_description = "Кількість товарів"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "get_photo",
        "title",
        "category",
        "quantity",
        "price",
        "created_at",
        "size",
        "color",
    ]
    list_editable = ["price", "quantity", "size", "color"]
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["title", "price"]
    list_display_links = ["pk", "title"]
    inlines = (GalleryInline,)

    def get_photo(self, obj):
        if obj.images.all():
            return mark_safe(
                f"<img src='{obj.images.all()[0].image.url}' width='75'>"
            )
        else:
            return "-"

    get_photo.short_description = "Мініатюра"
