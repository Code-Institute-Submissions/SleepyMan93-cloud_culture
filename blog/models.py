from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    subtitle = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField(max_length=20000)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.title)


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=100, db_index=True)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
