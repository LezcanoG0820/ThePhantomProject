from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django_currentuser.db.models import CurrentUserField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
# Create your models here.

class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'
        
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

#class producto, este va a detallar las especificaciones del producto
#debe usarse tambien en caso de añadir como de mostrar en pantalla
#debe de tener nombre, descripcion, precio, imagen y categoria

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        ordering = ["name"]
        
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default='generic description')
    image = models.ImageField(upload_to="media")
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/category/{self.slug}"
    
    @property
    def get_products(self):
        return Products.objects.filter(categories__title=self.title)
    

class Product(models.Model):
    
    class Meta:
        verbose_name_plural = 'Product Profiles'
        verbose_name = 'Product'
        ordering = ["category"]
    
    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default='generic description')
    details = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(upload_to="media")
    is_active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=1.00)
    category = models.ForeignKey(Category, default=False, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.name} {self.category}'

    def get_absolute_url(self):
        return f"/product/{self.slug}"
    

class Review(models.Model):
    
    class Meta:
        verbose_name_plural = 'Reviews of Products'
        verbose_name = 'Review'
        ordering = ['timestamp']
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, default='TITLE')
    content = RichTextField(max_length=5000, default='review')
    score = models.DecimalField(max_digits=2, decimal_places=1, default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
