from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    category= (
        ('Fiction','Fiction'),
        ('Non-Fiction','Non-Fiction'),
        ('Science Fiction','Science Fiction'),
        ('Fantasy','Fantasy'),
        ('Mystery','Mystery'),
        ('Romance','Romance'),
        ('Horror','Horror'),
        ('Biography','Biography'),
        ('Autobiography','Autobiography'),
        ('Self-Help','Self-Help'),
        ('Cookbook','Cookbook'),
        ('Poetry','Poetry'),
        ('History','History'),
        ('Science','Science'),
        ('Art','Art'),
        ('Travel','Travel'),
        ('Children','Children'),
        ('Young Adult','Young Adult'),
        ('Other','Other'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100 , null=True) 
    price = models.FloatField()
    category = models.CharField(max_length=50,choices=category)
    published_date = models.DateField(null=True)
    is_bestseller = models.BooleanField(default=False)
    tags = models.ManyToManyField('Tag')
    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    order_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.customer_name
    
class Review(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()
    reviewer_name = models.CharField(max_length=100)
    reviewer_email = models.EmailField()
    review_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.reviewer_name