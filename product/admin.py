from django.contrib import admin
from product.models import Product, Review,Category, ProductImage
# Register your models here.


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Review)
admin.site.register(Category)