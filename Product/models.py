from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    is_navbar = models.BooleanField(default=True)
    p_category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="parent_category", null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.p_category == None:
            self.is_navbar = True
        else:
            self.is_navbar = False
        return super().save()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product Manufacturer"
        verbose_name_plural = "Product Manufacturers"

class Product(models.Model):
    discounts = (
        (5, '5'),
        (10, '10'),
        (15, '15'),
        (20, '20'),
        (25, '25'),
        (30, '30'),
        (35, '35'),
        (40, '40'),
        (45, '45'),
        (50, '50')
    )

    name = models.CharField(max_length=100)
    price = models.FloatField()
    in_sale = models.BooleanField(default=False)
    discount = models.IntegerField(choices=discounts, null=True, blank=True)
    new_price = models.FloatField(null=True, blank=True)
    overview = models.TextField()
    details = models.TextField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="product_manufacturer", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product_category")
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if self.in_sale:
            self.new_price = self.price - self.price*(self.discount/100)
        return super().save()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

class Color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} color"

    class Meta:
        verbose_name = "Product Color"
        verbose_name_plural = "Product Colors"

class Image(models.Model):
    image = models.ImageField(upload_to="product_images")

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"


class Size(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Product_version(models.Model):
    quantity = models.PositiveIntegerField()  ##
    review_count = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    read_count = models.PositiveIntegerField(default=0)
    cover_image = models.ImageField(upload_to="product_images")  ##
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name="product_color")  ##
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_version")  ##
    images = models.ManyToManyField(Image, related_name='images_of_products')
    size = models.ManyToManyField(Size, blank= True)  ##
    
    def __str__(self):
        return f"{self.product.name}'s {self.color.name} version"

    class Meta:
        verbose_name = "Product Version"
        verbose_name_plural = "Product Versions"
###################################


# class Product_version(models.Model):
#     cover_image=models.ImageField(upload_to="product_images")
#     quantity=models.PositiveIntegerField()
#     color = models.ForeignKey(Color, on_delete=models.CASCADE)
#     size = models.ManyToManyField(Size, blank= True)
#     product_id=models.ForeignKey(Product, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.product_id.name}'


# class reviews(models.Model):
#     Rates = [
#         (1, "20"),
#         (2, "40"),
#         (3, "60"),
#         (4, "80"),
#         (5, "100"),
#     ]
#     price_rating = models.IntegerField(choices=Rates)
#     value_rating = models.IntegerField(choices=Rates)
#     quality_rating = models.IntegerField(choices=Rates)
#     nickname = models.CharField(max_length=100)
#     review = models.TextField(verbose_name="Review")
#     summary = models.CharField(max_length=100)
#     dated = models.DateTimeField(auto_now=True)
#     product_id = models.ForeignKey(Product_version, on_delete=models.CASCADE)
    
#     class Meta:
#         verbose_name="reviews"
#         verbose_name_plural="reviews"
        
#     def __str__(self):
#         return self.nickname


###################################

class Review(models.Model):
    Rates = {
        (1, "20"),
        (2, "40"),
        (3, "60"),
        (4, "80"),
        (5, "100")
    }
    price_review = models.IntegerField(choices=Rates)
    value_review = models.IntegerField(choices=Rates)
    quality_review = models.IntegerField(choices=Rates)
    nickname = models.CharField(max_length=75)
    summary = models.CharField(max_length=50)
    product_review = models.TextField()
    review_date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product_version, on_delete=models.CASCADE, related_name="product_review")

    def __str__(self):
        return f"{self.nickname}'s reviews"

    class Meta:
        verbose_name = "Product Review"
        verbose_name_plural = "Product Reviews"

