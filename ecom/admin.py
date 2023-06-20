from django.contrib import admin

from ecom.models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(ColorVariant)
admin.site.register(SizeVariant)
admin.site.register(QuantityVariant)
admin.site.register(Product)
admin.site.register(Product_Image)


