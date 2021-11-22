from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_nicotine = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    """ A model for users to leave reviews on products """
    product_id = models.ForeignKey('Product', null=True, related_name='reviews',
                                   blank=True, on_delete=models.SET_NULL)
    review_title = models.CharField(max_length=30)
    review_text = models.TextField(max_length=280)
    review_date = models.DateTimeField(db_index=True, auto_now_add=True)
    review_user = models.ForeignKey(User, null=True,
                                    blank=True,
                                    on_delete=models.SET_NULL,
                                    related_name='review')

    class Meta:
        ordering = ['-review_date']

    def __str__(self):
        return self.review_title