from django.db import models

from django.utils.text import slugify

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


# def get_upload_path(instance, productname):
#     return os.path.join(str(instance.folder.uid), productname)


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name

class QuantityVariant(BaseModel):
    varient_name = models.CharField(max_length=100)

    def __str__(self):
        return self.varient_name

class ColorVariant(BaseModel):
    color_name = models.CharField(max_length=80)
    color_code = models.CharField(max_length=60)

    def __str__(self):
        return self.color_name

class SizeVariant(BaseModel):
    size_name = models.CharField(max_length=100) 

    def __str__(self):
        return self.size_name       



class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quentity_type = models.ForeignKey(QuantityVariant, null=True, blank=True, on_delete=models.PROTECT)
    color_type = models.ForeignKey(ColorVariant, null=True, blank=True, on_delete=models.PROTECT)
    size_type = models.ForeignKey(SizeVariant, null=True, blank=True, on_delete=models.PROTECT)

    product_name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='products')
    price = models.CharField(max_length=20)
    description = models.TextField()
    stock = models.IntegerField(default=100)


    def __str__(self):
        return self.product_name
    

class Product_Image(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='products')    
